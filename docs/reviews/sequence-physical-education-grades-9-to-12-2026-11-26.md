# Expert read: scope and sequence of Physical Education, grades 9 to 12 (2026-11-26)

Course `physical-education-grades-9-to-12`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), as
docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md ask. I did not write the scope.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/physical-education.md; docs/ADOPTION-BAR-SUBJECTS.md section 4;
  docs/courses/physical-education/APPROACH.md in full; the SEL shared-steps section of docs/courses/sel/STANDARD.md
  (section 7, the 9 to 12 forms); build/scope-writes/AFTERCORE-BRIEF.md.
- docs/courses/physical-education-grades-9-to-12/scope-and-sequence.md and data/plans/physical-education-grades-9-to-12/days.csv
  (all 320 rows: goal, codes, assess, school_day, retrieves and note), cold.
- Beside them: the frame (course in brief, Seams, Models carried, Units table, Course-level checks, Cross-subject,
  For the lead, Decided by Cory); data/progressions/physical-education.csv (grades 6 to 12 assumes);
  data/standards/shape-pe-2024.txt (the 43 span-12 indicators); data/plans/calendar.csv for grades 9 to 12 (PE,
  health 9 to 12, SEL 9 to 12); the CALENDAR.md table rows for this course; the SEL 9 to 12 frame's PE rows and its
  days.csv units 5, 14, 20, 21 and 22; the frame's 2026-11-25 Codex read.
- Gates: `plan.py check` (this course passes; failures elsewhere are other courses'), `frame.py calendar` (no PE 9
  to 12 clash lines), `sequence.py check` (0 failures; 12 notes "standard None is on no day" for units 13 to 24,
  which own nothing by the frame, so the notes are harmless), `frame.py check` (0 failures; 74 unit days a year),
  `stale.py check` (121 files, 0 failures). The gate's rule 2 count prints no readiness or retrieval notes.
- Sources opened: CDC "Preventing Drowning" (opened; dated Sept. 29, 2025); National Weather Service "Cold Water
  Hazards and Safety" (opened); ActiveSG's sepak takraw page (opened). Browser check: the National Football Museum's
  1863 laws page (403) and the IOC history page (timed out twice).

## Verdict

The scope is sound and close to buildable: every owned indicator sits on a day inside its owner unit, every unit and
course-level check falls in the frame's and CALENDAR.md's weeks, readiness and retrieval match the progression and
the gate, and the safety, water, body and cultural guards are carried day by day. The biggest risk is the
64-session path, which drops every practice day of eight owned indicators (S3.12.1, S3.12.2, S2.12.13, S2.12.1,
S2.12.2, S3.12.6, S4.12.1, S4.12.8), so on that path they go from first teaching straight to the check. The one
change that matters most is naming, on each of those drop days, which kept day absorbs the practice; close behind,
the 24 course-level check and respond days carry no space or equipment line, and several checks claim codes no
prompt asks.

Findings: 8 (1 serious, 4 moderate, 3 minor).

## Findings, most serious first

### 1. The 64-session path drops the only practice of eight owned indicators (serious)

LAYER sequence. REPEAT yes (the computer science grade 10 read of 2026-11-26, finding 3, is the same kind).
Confidence: firm (counted from days.csv; the frame's rule says the drops are "practice days only" and every owned
outcome "stays taught").

What is wrong: counting every non-check day that carries a code, and removing the 64 days the notes mark "dropped on
the 64-session path", these owned codes keep only their Understanding day before the check:

| Unit | Code | Days that carry it | Kept on the 64 path |
|---|---|---|---|
| 1 | S3.12.1, S3.12.2 | 8 (U), 9 (A); S3.12.2 also 1 | 8 (and 1) only |
| 3 | S2.12.13 | 30 (U), 32 (A) | 30 only |
| 4 | S2.12.1 | 45 (U), 48 (A) | 45 only |
| 4 | S2.12.2 | 46 (U), 47, 48 (A) | 46 only |
| 10 | S3.12.6 | 122, 124 (U), 129, 130 (A) | 122, 124 only |
| 12 | S4.12.1 | 142 (U), 143 (A), 145 (F) | 142 only |
| 12 | S4.12.8 | 146 (U), 148 (F), 151 (A) | 146 only |

Unit 12 is the worst case: days 148 and 151 are the only days a student uses the chosen emotion strategy in a hard
moment, and the check (day 155) scores "a judgment after using it" and watches the strategy "used in a hard moment".
On the 64 path the student meets the hard moment for the first time at the check. Day 32 is also the frame's kept
candidate (the before-and-after change) and the only day S2.12.13's "improve" half is practiced. Conduct for S3.12.1
and S3.12.2 is "marked from the record kept during practice", and day 9 is most of that record.

Why it matters: a teacher on the short path (the frame's own default for a school with fewer sessions) would score
skills the students never practiced, which breaks "nothing assessed and no owned part cut".

The fix (the counts are tight: grade 9, 10 and 12 drops sit at the frame's caps, so moving drops between units does
not work; fold the practice into kept days instead and say so in each drop day's note and in the Shorter path
section):
- Day 9: on the 64 path, day 10's twelve-minute session runs with partners and the courtesy card, so the S3.12.1 and
  S3.12.2 record is kept there.
- Day 32: the before-and-after change runs inside day 34's rehearsal (one change, a partner watching).
- Day 48: day 49's rehearsal ends with one tactic named and used per game (S2.12.1 and S2.12.2).
- Days 129 and 130: day 131's control leg runs with the safety checklist kept (S3.12.6).
- Days 143, 145: day 154's rehearsal runs the expressive block at the chosen level.
- Days 148, 151: day 147's social block ends in a hard moment with the chosen strategy used and judged in one line,
  and day 154 repeats it.
Where a note already says "its cue returns in the next instant activity", replace that line on these days with the
named kept day, since an instant activity is too short to stand for a hard moment or a led tactic.

### 2. The 24 course-level check and respond days name no space, equipment or wet-weather path (moderate)

LAYER sequence. REPEAT new. Confidence: firm (counted).

What is wrong: days 38 to 40, 78 to 80, 118 to 120, 158 to 160, 198 to 200, 238 to 240, 278 to 280 and 308 to 310
are the only days with no space line. Several are movement-heavy and sample hazards: day 158 runs an orienteering
leg and a life jacket station in finals week; day 118 a sepak takraw rally and skill-related drills (landings);
day 78 a strength station; days 198 and 278 the students' chosen activities.

Why it matters: the AFTERCORE brief says every movement day names its safe space and equipment, and the safety read
works from these notes. A writer building day 158 from this row has no route, weather, group or water rule.

The fix: give each check and respond day the space line of each unit it samples, joined (for example day 158: "the
route on or next to school grounds checked by the teacher, students in groups, water, shade and the school's cold
and heat rules, wet weather the indoor map course; dry land only for the life jacket station, adult and youth
sizes").

### 3. Checks claim codes that no prompt asks (moderate)

LAYER sequence. REPEAT yes (the computer science grade 10 read, findings 1 and 2: a prompt per part). Confidence:
likely (read as a busy writer would).

What is wrong:
- Unit 12, days 155 and 156, claim S4.12.3 and S4.12.4 (find activity that improves health; pick activity that
  matches interests). The knowledge task lists the log, the plan, the S4.12.7 prompt, the emotion comparison and the
  reflection; no prompt asks which health part each block improves or which interest it matches.
- Day 308 (grade 12 year-end) claims S2.12.15, S2.12.16, S3.12.7 and S3.12.1. Its items are "an active adult week's
  balance and a barrier plan" and "the main point of a leadership evaluation" (S3.12.8); nothing names the week's
  technology or food, nothing asks a student to reason through a challenge, and the conduct line ("courtesy with
  guests, carried from the event") is S3.12.2 evidence already scored at unit 22's end.
- Day 158 (grade 10 year-end) claims S3.12.7, "reason through challenges alone and in teams"; its item asks only the
  group problem at a control.
- Days 172, 198, 252 and 278 claim S1.12.1 to S1.12.4 (and day 172 also S2.12.1 to S2.12.4) for one chosen activity
  each. A student who chose badminton shows S1.12.2 and S2.12.2, not all four.

Why it matters: the record would credit indicators a student was never asked about, and a later course page
would claim them.

The fix: day 155 adds one prompt, "for each block, the health part it builds and the interest it matches";
day 308 adds an item on the invented graduate's week naming one technology and one food choice with a reason, and
one "what would you try next" item on a pictured challenge, and drops S3.12.1 from its codes (or names a new
awareness item); day 158 adds the individual half ("what you would change in your own pace at that control"); on
days 172, 198, 252 and 278 the note says the code marked is the one matching the student's chosen activity (one of
S1.12.1 to S1.12.4, and on day 172 the matching S2 tactic code), and the course page claims those codes only as
"used in new settings", which the frame already does.

### 4. A few owned parts get one day of teaching (moderate)

LAYER sequence (the load comes from the frame's unit 12). REPEAT new. Confidence: likely.

What is wrong, with counts: unit 12 owns nine indicators in 13 teaching days. S4.12.3 and S4.12.4 sit only on day
144 (one Understanding day, shared with S4.12.5); S4.12.9 only on day 153. In unit 8, S2.12.5 and S2.12.11 sit only
on day 98. Compare unit 3, which spends 10 teaching days on two indicators. Each of these is scored at the unit's
check two to seven days later with no day of use.

Why it matters: the indicators "find and join" (S4.12.3) and "pick and join" (S4.12.4) ask for joining an activity,
not only naming a fit; a single talk day does not reach them.

The fix, with no day added: tag days 145 and 147 (the expressive and social blocks) S4.12.3 and S4.12.4, with a
private log line per block naming its health part and interest; tag day 154 S4.12.9 with the reflection's two
examples drafted beside the rehearsal (the reflection is scored, so it should have a draft); tag day 100 (the
student-chosen block) S2.12.11 with one line on what the block gives an adult; tag day 101's mid-way check S2.12.5
with one line on how the plan could shape a week after school.

### 5. Unit 11's source line overclaims what CDC's page says (moderate)

LAYER sequence. REPEAT yes (the frame's Codex read noted CDC's page "is not a complete rescue-teaching" source).
Confidence: firm (both pages opened 2026-11-26).

What is wrong: day 137 teaches cold-water shock, currents, hypothermia and calling for help with "Source: CDC's
Preventing Drowning page". The CDC page (dated Sept. 29, 2025) covers life jackets and hidden hazards in natural
water such as currents; it does not mention cold-water shock, hypothermia, or reach and throw rescues.

Why it matters: bar criterion 4 asks that fitness and safety content be accurate and sourced; a teacher page citing
CDC for cold-water shock would not hold up.

The fix: day 137's source line names CDC for life jackets and currents, and the National Weather Service's "Cold
Water Hazards and Safety" page (https://www.weather.gov/safety/coldwater, opened 2026-11-26) for cold shock and
hypothermia; reach and throw stay marked "from memory, the safety agent to confirm" until the safety read names a
rescue source (for example a national lifesaving body's page).

### 6. Readiness checks sit on the first day of units 7, 13 and 19 (minor)

LAYER process. REPEAT yes (LEAD-ITEMS already lists the gate item). Confidence: firm.

What is wrong: the brief asks the read to name any readiness check on the first day of a unit other than unit 1.
Day 81 (unit 7, g7-skill-fitness-use) and day 241 (unit 19, the no-grade-11 fallback) carry one in the note, as
the frame sets them; day 161 (unit 13) carries one for a grade 11 elective taken in grade 12.

Why it matters: little in practice. The rule's alternative (the last ten minutes of the year before) would sit a
summer ahead, which is worse; the scope says so under For the lead 1.

The fix: none in the scope. The lead settles the rule exception for a level's first unit (a year's first day after
its hook), and the gate then accepts `readiness` in the assess cell for days 81, 161 and 241.

### 7. Day 180's SEL link points at the wrong course year (minor)

LAYER sequence. REPEAT new. Confidence: firm.

What is wrong: day 180 (grade 11, week 8) says "PE first: SEL 9 to 12 unit 14 (weeks 6 to 11) opens with rest and
sleep in a plan". SEL unit 14 runs in the same weeks and its days open on goal and coping retrieval, not rest; the
SEL frame ties g11-sm-calm-down to PE's g10-rest in grade 10 unit 8, a year before, and grade 11 PE is elective.

The fix: move the line to day 93 (grade 10 unit 8's rest day): "PE first: SEL 9 to 12 unit 14 (grade 11) may open
with this rest-and-sleep plan as retrieval"; drop it from day 180.

### 8. Two small retrieval gaps against the progression (minor)

LAYER sequence. REPEAT new. Confidence: firm (assumes counted from data/progressions/physical-education.csv).

What is wrong: unit 4's rows assume g8-striking-fielding-play; day 42 retrieves the other grade 8 game rows but not
this one. Unit 23's rows assume g11-fitting-challenge; day 296 retrieves g11-plan-for-self and g11-express-company
only. The gate passes (it counts differently), so these are notes, not faults.

The fix: add g8-striking-fielding-play to day 42's retrieves (the target golf swing from unit 3 already gives the
setting), and g11-fitting-challenge to day 296's.

## What is right and should not be touched

- school_day = 2 x course day per year: every unit and check sits on the frame's weeks (mid-year week 16, year-end
  week 32, grade 12 year-end week 28), and calendar.csv agrees.
- Each owned code's days sit inside its owner unit; grades 11 and 12 claim nothing owned, and their notes say "used in
  new settings".
- Readiness rows match the progression's last use (g6-analyze-skill, g7-dance-ideas, g7-skill-fitness-use, g7-rest,
  g7-eat-move-well and the grade 8 rows first met again in grade 10), each in the last ten minutes of the previous
  unit's respond day or the mid-year respond day; the grade 12 fallbacks for a student without grade 11 are complete.
- Collect once is handled with care: every course-level check after a unit carries that unit's record unscored and
  moves its items to earlier content or an invented case, and says so in the note.
- Shared cards are quoted word for word in the 9 to 12 form (goal steps on days 65, 149, 202, 256; coping plan on
  days 68, 146, 272).
- Safety: no maximal lift, bands and body weight, spotters only under the school's own staff, dry land only for
  water, swing lanes one direction, foam balls, no headers in sepak takraw, landings on soft surfaces.
- Body and emotion guards: no weighing, body, calorie or diet talk; private, ungraded fitness records; calm steps
  offered never as punishment; the counselor named; no student asked to share a reflection aloud.
- Cultural guards: bhangra stays a candidate until the sensitivity confirm (Cory confirmed the pick); sepak takraw is
  labeled modified; no sacred or ceremonial game; unit 22's pick is read with its source before the event.
- Facts checked: sepak takraw's basic play (three a side, no hands or arms) matches ActiveSG, and the classroom form
  is labeled modified; the 1863 date for the Football Association's laws and the 1896 Athens revival agree with my
  memory (pages marked browser check below).
- Health and SEL leans sit after the other course's unit in calendar.csv (health 9 to 12 units 2, 6 and 15 in grade
  9 weeks 1 to 12; SEL units 1, 20, 21 and 22) or carry their fallback; the spring-health path is in day 66.

## What I could not judge

- The IOC history page (1896 revival and women's later entry) and the National Football Museum's 1863 laws page:
  browser check, both refused an automated read.
- Bhangra at a Punjabi or Indian cultural institution's page: the sensitivity agent's job, still open as the frame
  says.
- MVPA share per day: the day rows do not give minutes; the unit plans must show at least half moving.

## Sources

- https://www.cdc.gov/drowning/prevention/index.html : what CDC's page covers for unit 11 (life jackets, currents;
  dated Sept. 29, 2025).
- https://www.weather.gov/safety/coldwater : cold shock and hypothermia, the source finding 5 proposes.
- https://www.activesgcircle.gov.sg/learn/sepak-takraw/rules-and-regulations-of-sepak-takraw?tab=how_to_play : unit 9's
  basic play.
- https://nationalfootballmuseum.com/items/the-laws-of-the-game-1863/ : browser check (403).
- https://www.olympics.com/ioc/history : browser check (timed out).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| On the 64 path, fold the dropped practice of days 9, 32, 48, 129 and 130, 143 and 145, 148 and 151 into days 10, 34, 49, 131, 154 and 147 (finding 1) | Keeps every owned part practiced with the caps unchanged | days.csv notes; scope-and-sequence.md Shorter path |
| Add each sampled unit's space line to the 24 check and respond days (finding 2) | Every movement day names its space and gear | days.csv |
| Add the prompts named in finding 3 to days 155, 158 and 308; drop S3.12.1 from day 308's codes; mark one chosen-activity code per student on days 172, 198, 252, 278 | A prompt per part of each claimed code | days.csv |
| Retag days 100, 101, 145, 147 and 154 as in finding 4 | Gives S2.12.5, S2.12.11, S4.12.3, S4.12.4 and S4.12.9 a day of use, no day added | days.csv |
| Day 137's source line: CDC for life jackets and currents, the National Weather Service cold-water page for cold shock and hypothermia, reach and throw "from memory" until the safety read | Sources say only what they say | days.csv; the unit plan |
| Move day 180's SEL line to day 93 | The SEL frame ties it to grade 10 unit 8 | days.csv |
| Add g8-striking-fielding-play to day 42 and g11-fitting-challenge to day 296 retrieves | The progression's assumes | days.csv |

## For Cory

- Nothing this read. Every finding is inside the frame's units and the standards' limits.

## For the source list

- National Weather Service, "Cold Water Hazards and Safety", https://www.weather.gov/safety/coldwater (free, opened
  2026-11-26): cold shock and hypothermia; advice for the person in the water, not rescuers.

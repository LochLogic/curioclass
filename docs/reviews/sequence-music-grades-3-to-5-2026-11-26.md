# Expert read: scope and sequence of Music, grades 3 to 5 (2026-11-26)

Course `music-grades-3-to-5`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write
the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9
  and "Fails if"), docs/courses/arts/STANDARD.md and docs/courses/arts/APPROACH.md in full, and
  build/scope-writes/ARTS-BRIEF.md.
- docs/courses/music-grades-3-to-5/scope-and-sequence.md and data/plans/music-grades-3-to-5/days.csv (all 192 rows),
  read cold.
- Beside them: the frame (docs/courses/music-grades-3-to-5/frame.md, all of it), the mu-g2 to mu-g5 rows of
  data/progressions/arts.csv, the 63 grade 3 to 5 music lines of data/standards/ncas-performance-standards-words.txt,
  the course's rows in data/plans/calendar.csv and CALENDAR.md, the math grade 3 to 5 and ELA grade 3 and 4 rows of
  calendar.csv that the leans name, and the music K to 2 scope and days (written this morning) for the seam.
- Earlier reads for repeats: docs/reviews/sequence-media-arts-grades-3-to-5-2026-11-26.md (the first arts scope
  read, same brief) and the frame reads it names.
- Gates: `scripts/sequence.py check music-grades-3-to-5` 0 failures; `scripts/plan.py check` has no failure for
  this course (its failures are algebra-ii items); `scripts/frame.py calendar` puts this course's checks in weeks 15
  and 24 of grades 3, 4 and 5, as CALENDAR.md's table does; `scripts/stale.py check` 0 failures. A short script over
  days.csv confirmed every one of the 63 ids sits only in its own year, on at least one teaching day and on an
  end-of-unit or check row; it also counted the teaching days per id (finding 4).
- No outside source was opened. The id meanings rest on our own-words file (checked at source by earlier arts
  reads); timing and room judgments rest on APPROACH and on memory of elementary music specials, marked so.

## Verdict

Sound in shape: the band-year rule is stated once and kept (21 ids a year, 63 in all, each year headed with its
grade), every unit has a technique shown with a step card before the making, one critique by the describe, ask,
suggest routine, a revision and a showing before its end-of-unit assessment, the works range across five continents
and many centuries with living makers each year, and every check sits on its CALENDAR.md week. The biggest risk is
the assessment wording a unit writer would copy: about a third of the end-of-unit items ask for one part of an id
whose words line names several ("one loudness or speed difference", "an interest, an experience or a purpose"), and
the Re8 items drop the "and you" part entirely. The one change that matters most is the item wording in finding 1,
settled below; the second is the once-a-week merge order in the listening units (finding 2), which has the class sing
its chosen song before it chooses it.

## Findings, most serious first

### 1. Many end-of-unit items ask for one part of a code whose words line names several

LAYER sequence and frame (the evidence lines come from the frame's Units table). REPEAT yes (part coverage, as in
the media arts 3 to 5 read, finding 4). Confidence: firm against the words file.

- **What is wrong.** The brief asks every end-of-unit and check task to ask about each part of each code it lists.
  These items do not:

  | Id | Item now (days.csv check notes, scope assessment lines) | Part not asked | Item that asks every part |
  |---|---|---|---|
  | MU:Re8.1.3a | "one loudness or speed difference" (days 29, 47) | loudness and speed both | one loudness difference and one speed difference, each with what it shows |
  | MU:Re8.1.4a | "one tone color choice and what it carries" (days 93, 111) | loudness, speed; "and you" | one line each for loudness, speed and tone color on the unseen recording; plus one talk item at the teacher's spot: how your group used one of them to show what the song means (unit 6 has no talk items now, so the two-item limit holds) |
  | MU:Re8.1.5a | "one articulation choice" (days 157, 175) | loudness, speed, tone color; "and you" | one line each for the four on a tick-and-word card (reading load: one short card); the same talk item on the group's own choice |
  | MU:Re7.1.3a, 4a, 5a | log page on "an interest, an experience or a purpose" (or context) | the other parts | one line per part: three in grade 3 (interests, experiences, purposes), four in grades 4 and 5 (adding contexts), with one piece of evidence from the music in grade 5 |
  | MU:Pr4.1.3a, 4a, 5a | kept card: "three reasons (interest, knowledge, purpose or setting)"; grade 4 and 5 "one of them the class's skill" | purpose or setting; the rest in grades 4 and 5 | one reason per factor: interest, knowledge, purpose, setting (3); interest, knowledge, setting, the class's skill (4); interest, knowledge, setting, own and others' skill (5) |
  | MU:Cn10.1.3a, 4a, 5a | talk item: "one taste, piece of knowledge or skill" | two of the three | one talk item on the frame "I like ___, I know ___, I can ___, so I chose ___" (own, invented or public, marked the same) |
  | MU:Cn11.1.3a, 4a, 5a | talk item: "one tie ... another art, subject or daily life" | other arts, subjects, settings, daily life as separate parts | one talk item on a four-box card (another art, a school subject, a different setting, daily life), a few words in each box |
  | MU:Cr1.1.4a, 5a | "a phrase improvised over the drone" or "over I and V" | harmony ideas improvised | the student improvises the harmony choice too: picks and holds the drone note or a third under the tune (4); chooses where the chord changes from I to V (5) |
  | MU:Cr2.1.4a, 5a | "a sentence on what its sections are for" / "what it is for" | context | add "and where it would be heard" to the sentence (day 96 and 160 already teach it) |
  | MU:Pr4.2.5a | "one way the harmony and the form work" (day 189) | timing, pitch | score the kept marked score for timing and pitch, as year 4 does on day 125, and keep the card for harmony and form |
  | MU:Pr4.2.5c | "one way history or culture shaped a performance" (day 142) | society; the two as separate parts | three lines (history, culture, society), written alone in the first ten minutes of day 142 before the supported practice starts |
  | MU:Pr4.2.3b | "an unseen four-bar rhythm and short tune" (day 61) | picture and standard notation both | the unseen card shows two bars in picture notation and two in standard |

- **Why it matters.** A unit writer copies these lines into the guide and the record sheet. A student can be marked
  met on an id after showing a third of it, and the record then says the grade's standard was met when it was not.
  Re8's "and you" (the student's own expressive choices) is the part that ties listening to the student's making;
  dropping it leaves a listening quiz.
- **The fix.** Settled below: the right-hand column becomes the item wording in days.csv (the check-day notes, days
  14, 15, 29, 47, 61, 78, 79, 93, 111, 125, 142, 143, 157, 175, 189) and in the scope's assessment lines and
  "Course-level checks". For the lead: the frame's Units table evidence lines and its Course-level checks table
  carry the old wording and should be brought into line in the frame fix pass, so the unit writer sees one wording.

### 2. The listening units use the three-prompt card before teaching it, and their once-a-week merges run out of order

LAYER sequence. REPEAT yes (used before taught; the once-a-week path not holding, as in the media arts read,
finding 2). Confidence: firm.

- **What is wrong.** Three things, all in the listening units (1, 5, 9), whose days share one pattern:
  - Day 4 (and 68, 132), a Fluency day, has the class "answer the three-prompt listening card"; the card (a feature
    of the form, a musical element, the setting) is first taught on day 5 (69, 133). In year 3 the form words
    (verse, chorus, call and answer) are new that week.
  - The once-a-week table merges 3+4+7 into session 2. Day 7 sings "the chosen song", but the class chooses it on
    day 6, in session 4.
  - It merges 10+12 into session 5. Day 12 runs "the chosen song with its change", but the change is made on day 11,
    in session 6.
- **Why it matters.** A teacher on the once-a-week path, which the brief says must hold, is told to rehearse a song
  the class has not picked and a revision it has not made. On the full path, a grade 3 student meets a new response
  card cold.
- **The fix.** Settled below. Swap the goals and notes of days 4 and 5 (68 and 69, 132 and 133, with the ELA lean row
  moving to day 132): the study day comes first and the practice day, with the baseline look, second, which APPROACH
  allows (the baseline is "during the unit's first practice days"). Then the listening merges become: 1+2; 3+4; 5+6;
  7+8+9; 10+11; 12+13+14; 15; 16. That is still 8 sessions; the Fluency days (5, 7, 12) fold into their session's
  opener as the frame says; the critique and the revision share session 5, and the showing follows them.

### 3. Rows used earlier in a year than their retrieval day

LAYER sequence. REPEAT yes (retrieval missing, as in the media arts read, finding 5). Confidence: firm.

- **What is wrong.** Each unit retrieves its own two rows on day 2, but the listening units lean on other year-before
  rows sooner, with nothing in `retrieves`:
  - Day 11 (75, 139) has students "make up a short clapped or sung opening": the invent row (mu-g2-invent,
    mu-g3-invent, mu-g4-invent), retrieved only on day 18 (82, 146).
  - Days 8 and 10 (72 and 74, 136 and 138) run the critique routine: the revise row (mu-g2-revise and so on),
    retrieved only on day 32 (96, 160). Day 8's note says "entry reteach", but the column is empty.
  - Day 3 shows rhythm syllables and beat counts "again", and day 33 and 35 write rhythm and a tune on the staff
    "building on grade 2's so, mi and la": the read row (mu-g2-read), retrieved only on day 50. Year 4 day 97 and
    year 5 day 161 write rhythm by note values (mu-g3-read, mu-g4-read), retrieved only on days 114 and 178.
- **Why it matters.** Rule 2: a row used the year before opens as a retrieval task inside the day that uses it. A
  student new to the band, or a mixed class running the years in turn, meets improvising and the critique routine
  with no reteach.
- **The fix.** Settled below. Fill `retrieves` and put a short retrieval in the opener of: day 3 (mu-g2-read), day 8
  (mu-g2-revise), day 11 (mu-g2-invent), day 33 (mu-g2-read); day 72 (mu-g3-revise), day 75 (mu-g3-invent), day 97
  (mu-g3-read); day 136 (mu-g4-revise), day 139 (mu-g4-invent), day 161 (mu-g4-read). The day 2 retrievals stay; the
  scope's Readiness table gains these rows.

### 4. Six ids are taught on one day each, and three of those days are hooks

LAYER sequence. REPEAT new. Confidence: likely.

- **What is wrong.** Counted from days.csv: MU:Pr4.2.3c, 4c (how setting shapes a performance) sit only on the
  concert unit's hook day (49, 113); MU:Pr4.2.3a, 4a, 5a (the form or structure) only on day 50, 114 or 178; MU:Cn11.1.3a,
  4a, 5a only on day 9, 73 or 137. Each is then scored ten or more days later. The concert units give MU:Pr4.2.3b six
  days and the Pr6 ids four.
- **Why it matters.** A day that opens a unit carries the hook and the question; an id whose only teaching is that
  day is taught in what is left. A grade 3 student meets the Cn11 talk item after one lesson on it.
- **The fix.** Settled below, codes added to days that already do the work: MU:Pr4.2.3a on day 53 (the round
  entries are form), MU:Pr4.2.3c on day 58 (manners for the setting and venue); MU:Pr4.2.4a on 117, MU:Pr4.2.4c on
  122; MU:Pr4.2.5a on 183 (timing and harmony in the bar); MU:Cn11.1.3a on days 12 and 14 (one tie on the
  listening-log page), MU:Cn11.1.4a on 76 and 78, MU:Cn11.1.5a on 140 and 142. Each fold-in day of the short year
  (12, 76, 140) still has a second day for the id, so no owned part rests on a fold-in day alone.

### 5. The mid-year check's written card holds too much for six minutes and one short card

LAYER frame. REPEAT new. Confidence: likely (from the frame's own timetable and the reading-load rule).

- **What is wrong.** Days 29, 93 and 157 give six minutes to "the unseen recording played twice and its written
  card", but the card carries the unit's Re8 item (two readings of one tune, each played twice) and the earlier
  unit's sample (the three-prompt card and the criteria, on "a new open recording"). That is three excerpts played
  twice, then a card with about five prompts, for grade 3 readers limited to one short card (APPROACH "Reading
  load"). Finding 1's fix adds lines to the Re8 part.
- **Why it matters.** A teacher who keeps to the timetable cuts the sample or the listening; one who keeps the
  listening runs into the group time at the teacher's spot.
- **The fix.** Settled below, inside the day: the earlier unit's sample uses the second of the two readings as its
  recording, so there are two excerpts, under a minute each. For the lead (the frame's timetable): move the
  three-minute self-check into the time students wait while other groups are at the teacher's spot, so the card
  has nine minutes; or take the unit 1, 5 and 9 sample down to the setting prompt only.

### 6. The once-a-week opening session of the inventing units is the heaviest of the year

LAYER sequence. REPEAT yes (the media arts read, finding 2, the same kind). Confidence: likely.

- **What is wrong.** Session 1 of units 2, 6 and 10 is 17+18+19: the hook with two works compared (two pianists, or
  Ulali, or Márquez), the ten-minute retrieval, a new technique in named steps (call and answer, the drone, the I and
  V chords) and its drill. After set-up, clean-up and the retrieval about 21 minutes remain for a work and a
  technique. Session 6 (day 28) holds only a hand-in and a self-check.
- **Why it matters.** The lens's first rule is technique taught in steps; here it gets a few minutes on the path
  many schools will run.
- **The fix.** Settled below: inventing merges become 17+18; 19+20; 21+22; 23+24; 25+26; 27+28 (still 6 sessions).
  The critique (24) and the revision (25) sit in consecutive sessions, the showing (26) after the revision, and the
  kept card is handed in on the last session as now. The concert units' 51+52+53 (bar fractions, the tune on the
  staff and the second part) is heavy too, but the unit has no light session to trade with; I leave it, a judgment
  call.

### 7. Three flagged works have no sensitivity line on their day

LAYER sequence. REPEAT yes (the media arts read, finding 7). Confidence: firm (the frame's "Sensitivity reads" names
each).

- Day 31 names Cotten's flag but not the Brazilian music the frame lists for unit 3 (Villa-Lobos); day 49 has no line
  for Sweet Honey in the Rock (unit 4's listed community); day 145 has none for son and danzón of Mexico and Cuba
  (unit 10). A unit writer reads the day row first.
- **The fix.** Settled below: one line on each day, in the form the other days use ("the agent reads the group's or
  a cultural body's page first").

### 8. Some processes live only in a note line

LAYER sequence. REPEAT new. Confidence: likely.

- Connect in the composing and concert units (3, 4, 7, 8, 11, 12) sits only in the note of the hook day
  ("Connect (practice, not claimed)"), and create in the listening units only in day 11's (75's, 139's) note. The
  bar asks for all four processes in the course, which holds; the brief asks for them in every unit, which holds by
  a note. A writer building from the goal column drops them.
- **The fix.** Settled below: put the connecting tie into the goal of days 31, 49, 95, 113, 159 and 177, and the
  making into the goal of days 11, 75 and 139 (it is there already for 11; keep it, and name the meter it is made in).

### 9. Stale and miscopied text

LAYER sequence. REPEAT yes (note text a writer would copy wrong, media arts read finding 8). Confidence: firm.

- "Music K to 2 has no scope and sequence yet" (Readiness section) and For the lead 4 are stale: its scope and days
  were written this morning. I checked its days.csv: the eight grade 2 rows sit in its units 9 to 12 as this scope's
  Readiness table says (read 129 to 162, express and choose 145 to 162, invent and document 163 to 178, revise and
  perform 179 to 192), and day 134 teaches so, mi and la on a three-line staff card, which day 35 here builds on.
- Days 47, 111 and 175 and the scope's check sections say "units 1 and 2 (5 and 6, 9 and 10) sampled", but the one
  card asks MU:Re8.1.xa, a unit 2 (6, 10) id; the listening unit was sampled at mid-year. Say so.
- The scope and days.csv strip marks the frame keeps: Dvořák, Márquez, Danzón, Simón Bolívar, Angélique Kidjo,
  Toumani Diabaté, Ballaké Sissoko, "Funiculì, Funiculà", te reo Māori, Liliʻuokalani and "Aloha ʻOe". The ʻokina and
  the macron are part of the spelling in Hawaiian and Māori; a student page should carry them.
- Day 81's note has a stray ".;".
- **The fix.** Settled below.

### 10. Two school-day bases for the same days

LAYER process. REPEAT yes (media arts read, finding 11). Confidence: firm.

- days.csv counts `school_day` through the band (1 to 480); calendar.csv counts each year from 1 (unit 5 starts on
  school day 3 there, 163 here). The scope states the offset clearly and every check lands in the same week either
  way, so nothing is wrong for a teacher. For the lead: the same one-line decision as media arts, which count a later
  tool reads.

## What is right and should not be touched

- The band on one page: which grade's ids fall in which year, the mixed-class line, how `school_day` is counted, the
  64-day year, the logic model, the four processes by day.
- Technique before making in every unit: the call and answer, the drone, the I and V chords, the notation ladder
  and the practice card each have an Understanding day with a step card before the Application day that uses them.
- Order inside the composing and concert units: played before written, checklist before critique, critique before
  revision, revision before the share or the concert; reading before judged takes.
- The math leans: note values as parts of a bar wait for math grade 3's fractions unit (weeks 19 to 23) and start in
  week 26; year 5 counts whole and half beats until week 28, after math grade 5 unit 9 (weeks 24 to 27). Time
  signatures stay beats a bar in year 4.
- The checks: all six on weeks 15 and 24, standing as the inventing and composing units' end-of-unit assessments as
  the frame sets, with kept work scored once and response time counted once; the concert units assessed on their own
  two days in weeks 31 and 32, which are not course-level checks. The writer's `end` on the supported practice day
  and its For the lead 1 note are an honest answer to the gate; I agree with the proposed gate change.
- Candidate cells all settled with a reason and a day cost (five kept at no cost, one at ten minutes, three dropped,
  one conditional at no cost).
- The ten-days-short reading (ten school days, four sessions of a twice-a-week course) with four unassessed Fluency
  fold-ins a year, none of them a baseline day; the arithmetic is right.
- Works: each year has three or more continents, Native makers, living makers and works from the sixteenth century
  to 2012, each taught with its setting; the powwow, raga, Chickasaw and Hawaiian cautions are on their days.
- Safety: voice rest, set levels, no forced solos, adult-filled bottles and soft beaters are on the days that need
  them.

## What I could not judge

- Whether a classroom teacher with no music training can teach the relative minor (day 84) and the I and V chords by
  ear in one 40-minute session; a qualified music teacher's call (the lens says so).
- Whether six groups of five at the teacher's spot in 24 minutes, with the rest working quietly on listening logs,
  holds in a real grade 3 room; a trial would tell.
- The rights lines of the works the frame leaves to the unit plans.

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| Item wording as finding 1's right-hand column | each listed code asks each of its parts | days.csv notes of days 14, 15, 29, 47, 61, 78, 79, 93, 111, 125, 142, 143, 157, 175, 189; scope-and-sequence.md assessment lines and Course-level checks |
| Swap the goals and notes of days 4 and 5, 68 and 69, 132 and 133 (ELA lean row to day 132) | the three-prompt card is taught before it is practiced | days.csv; scope-and-sequence.md units 1, 5, 9 and Leans table |
| Listening merges 1+2; 3+4; 5+6; 7+8+9; 10+11; 12+13+14; 15; 16 | no session uses a pick or a change made in a later session | scope-and-sequence.md, Shorter path |
| Inventing merges 17+18; 19+20; 21+22; 23+24; 25+26; 27+28 | lightens the opening session, keeps 6 sessions | scope-and-sequence.md, Shorter path |
| `retrieves` and an opener retrieval on days 3, 8, 11, 33, 72, 75, 97, 136, 139, 161 | rule 2 for rows used before their unit's day 2 retrieval | days.csv; scope-and-sequence.md Readiness table |
| Codes added: Pr4.2.3a day 53, Pr4.2.3c day 58, Pr4.2.4a day 117, Pr4.2.4c day 122, Pr4.2.5a day 183, Cn11.1.3a days 12 and 14, Cn11.1.4a days 76 and 78, Cn11.1.5a days 140 and 142 | no id taught on one day alone, none only on a hook day | days.csv |
| Mid-year sample uses the second Re8 reading as its recording | two excerpts instead of three in six minutes | days.csv notes of days 29, 93, 157 |
| Sensitivity lines on days 31, 49, 145 | the frame flags each community | days.csv |
| Connect tie in the goals of days 31, 49, 95, 113, 159, 177; the made-up opening named in the goals of 11, 75, 139 | a process carried only in a note is easy to drop | days.csv |
| Readiness paragraph and For the lead 4 updated (K to 2 scope checked, matches); "unit 2 (6, 10) sampled; the listening unit at mid-year" on the year-end checks; diacritics restored; day 81's ".;" | stale or miscopied text | scope-and-sequence.md; days.csv |

## For the lead (not Cory)

- Bring the frame's Units table evidence lines and Course-level checks table into line with finding 1.
- Finding 5's timetable change (self-check in the waiting time, or a one-prompt sample).
- The writer's For the lead 1 (let scripts/sequence.py accept a check day that stands as a unit's end-of-unit
  assessment) and finding 10's school-day base, both shared with the other arts band scopes.
- The frame's open items 3 (spot-check the grade 3 to 5 words lines in Claude in Chrome) and the source-link pass
  stay open.
- Log the findings with `scripts/plan.py defect`, found_by `expert`; this read edits no file but this report.

## For Cory

Nothing new on scope, money, people or audience. The supplies ceiling stays where the frame puts it (frame "For the
lead" item 4).

## For the source list

None: no outside source was opened for this read.

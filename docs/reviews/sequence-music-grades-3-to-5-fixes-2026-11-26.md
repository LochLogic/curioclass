# Fixes: scope and sequence of music-grades-3-to-5, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-music-grades-3-to-5-2026-11-26.md), done as
docs/pipeline/briefs/sequence-fix.md with build/scope-writes/ARTS-FIX.md and ARTS-BRIEF.md. The Codex read waits for
Codex's usage reset (after 2026-11-30) and gets its own small pass. Files changed:
docs/courses/music-grades-3-to-5/scope-and-sequence.md and data/plans/music-grades-3-to-5/days.csv (written with a
Python csv script). frame.md is unchanged: no finding changes units, order, owned rows or day counts, and the frame's
wording changes the read asks for go to the lead below.

Counts: applied 26 (expert 10 of 10, with finding 5's timetable part passed on; lead calls 6; band items 1; own 9).
Not applied 2 (lead call 4, lead call 7: nothing to do here). Codex: none yet.

## Applied

- **Expert 1** (item wording, every part): days.csv notes of days 14, 15, 29, 47, 61, 78, 79, 93, 111, 125, 142, 143,
  157, 175, 189 now carry the read's right-hand column: Pr4.1 kept card one reason per factor (3, 4, 5 sets); Re7.1 log
  page one line per part, contexts added in 4 and 5, evidence in 5; Cn10 on the "I like, I know, I can, so I chose"
  frame; Cn11 on a four-box card; Re8.1.3a one loudness and one speed difference; Re8.1.4a and 5a one line per element
  (articulation on a tick-and-word card in 5) plus the "and you" part; Cr1.1.4a and 5a with the harmony choice
  improvised; Cr2.1.4a and 5a "and where it would be heard"; Pr4.2.3b two bars picture, two standard; Pr4.2.5a marked
  score scored for timing and pitch on day 189; Pr4.2.5c three lines written alone in the first ten minutes of day
  142. The .md gains one "Item wording" table under Course-level checks, and the unit and check sections cite it. The
  "and you" part of Re8 is a talk item at mid-year (as the read says) and, on the year-end checks (111, 175), a written
  line on the student's own group's piece: the share already holds talk items there, so a written line keeps the
  two-item limit.
- **Expert 2** (card before practice; once-a-week order): days 4 and 5, 68 and 69, 132 and 133 swapped (kind, goal,
  skills, codes, note): the study day comes first, the practice day with the baseline second. The ELA lean moved to
  day 132 (Leans table, unit 9 text, candidate line). Listening merges now 1+2; 3+4; 5+6; 7+8+9; 10+11; 12+13+14; 15;
  16, with the fold-in and critique order stated.
- **Expert 3** (retrievals): `retrieves` and a five-minute opener retrieval on days 3, 8, 11, 33 (mu-g2-read,
  mu-g2-revise, mu-g2-invent, mu-g2-read), 72, 75, 97 (mu-g3-revise, invent, read), 136, 139, 161 (mu-g4-revise,
  invent, read). Day 8's "entry reteach" wording replaced. Second Readiness table added in the .md.
- **Expert 4** (one-day ids): codes added on days that do the work, each goal saying so: MU:Pr4.2.3a day 53,
  MU:Pr4.2.3c day 58 (mu-g3-read added to skills), MU:Pr4.2.4a day 117, MU:Pr4.2.4c day 122 (mu-g4-read added),
  MU:Pr4.2.5a day 183, MU:Cn11.1.3a days 12 and 14, 4a days 76 and 78, 5a days 140 and 142. No fold-in day carries an
  id alone.
- **Expert 5** (mid-year card load): days 29, 93, 157: the earlier unit's sample uses the second of the two readings,
  so the card holds two excerpts. The frame timetable change goes to the structure pass.
- **Expert 6** (heavy inventing session 1): inventing merges now 17+18; 19+20; 21+22; 23+24; 25+26; 27+28. The concert
  units' 51+52+53 stays as the read left it, and the .md says why.
- **Expert 7** (sensitivity lines): day 31 (Brazilian music, Villa-Lobos), day 49 (Sweet Honey in the Rock), day 145
  (son and danzón of Mexico and Cuba), each in the "agent reads ... first" form.
- **Expert 8** (processes only in a note): the connecting tie is now in the goals of days 31, 49, 95, 113, 159, 177;
  the made-up opening "in the song's meter" is in the goals of 11, 75, 139.
- **Expert 9** (stale and miscopied text): Readiness paragraph and For the lead 4 now say Music K to 2's scope was
  checked and matches; year-end checks say "unit 2 (6, 10) sampled; the listening unit at mid-year" (days 47, 111,
  175 goals and notes; .md check sections and table); diacritics restored in both files (Diabaté, Ballaké, Angélique,
  Dvořák, Márquez, Danzón and danzón, Simón Bolívar, Funiculì, Funiculà, te reo Māori, Liliʻuokalani, Aloha ʻOe); day
  81's ".;" fixed.
- **Expert 10** (two school-day bases): settled by lead calls 5 and 8; the .md states the formula once and says a
  filled school_day wins.
- **Lead call 1**: For the lead 5 (the other reading of "10 days short") removed; four fold-in days a year kept.
- **Lead call 2**: the four-processes paragraph now says each year claims all four, a unit need not, no id outside the
  unit's owned rows, and practice on an existing day costs no day and claims no id.
- **Lead call 3**: Course-level checks says naming the unsampled codes with the reason is enough where the frame's
  check table limits the sample; For the lead 2 (the old L107 pick) replaced.
- **Lead call 5**: school_day kept band-long (1 to 480); the .md says so.
- **Lead call 6**: days 29, 93, 157 notes and the year 3 mid-year text: the group reading follows the unit's showing as
  the discipline's own evidence, with the check's own look-fors.
- **Lead call 8**: formula ceil(5n / 2) stated once; every unit and check checked by script against week =
  (school_day - 1) // 5 + 1: all 192 days sit on their year's week ceil(n / 2), checks on weeks 15 and 24 of each year.
- **Band item** (music 6 to 8 read, finding on two reteaches inside a ten-minute opener; the same wording was here):
  every unit's day 2 note now reads "Retrieval in the opener (10 minutes, five a row) ...; any reteach takes the next
  day's warm-up and first five minutes (whole class if more than a third missed, otherwise a small group)", after
  UNIT-PLAN rule 6; the .md's "Every day's 40 minutes" and mixed-class lines say the same. No other arts expert read
  has an "Across the band" section.
- **Own 1** (rule 2, retrieval written in prose): the day 2 notes of units 3, 4, 7, 8, 11, 12 (days 32, 50, 96, 114,
  160, 178) had `retrieves` filled but no line saying how; each now names its rows and the reteach.
- **Own 2** (each part, MU:Pr4.2.3c "personal and social"): day 61's card asks two lines, personal and social.
- **Own 3** (each part, MU:Pr4.2.4c "social and cultural"): day 125's card asks one line each.
- **Own 4** (each part, MU:Cr1.1.5a "social, cultural, historical context"): day 157's phrase item names the setting
  kinds.
- **Own 5** (teaching every part before it is assessed): Cn10 teaching days 6, 70, 134 now link a taste, a piece of
  knowledge and a skill on the frame; Cn11 teaching days 9, 73, 137 use the four parts on the four-box card.
- **Own 6**: four-processes table updated for the swap and the new codes (perform 5, 69, 133; connect 12, 76, 140).
- **Own 7**: unit sections name where the newly spread ids are taught (units 1, 4, 5, 8, 9, 12).
- **Own 8**: day 33's opener now holds the retrieval and the candidate listen, and says it runs ten minutes.
- **Own 9**: the .md's draft line points to this report.
- **Rule 2 lists re-run.** Earlier-grade rows: 24 day-2 retrievals and 10 in-unit retrievals, each one grade back, no
  readiness check owed; hook days (1, 17, 49 and their year 4 and 5 twins) use their unit's own technique and stay
  clean. Each check's sampled codes match the frame's table. Collect once: no child-by-child evidence is re-taken
  within ten days (kept work is scored once after the check). End days: no day asks two full performances. Our words:
  no base text in this course.

## Not applied

- **Lead call 4**: no gate baseline set here (gate.py not run for a baseline).
- **Lead call 7**: no frame check cell re-asks items a unit gave one to three days before (the mid-year checks stand
  as the inventing units' own assessments; the year-end Re8 card comes nine weeks after mid-year). Nothing to change.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A code's "and you" or self part on a year-end check goes on the written card as one line, not a talk item, where the share already holds talk items | keeps the two-talk-items limit |
| An in-unit retrieval of a year-before row is five minutes as the warm-up; two rows on a unit's day 2 take five minutes each; any reteach takes the next day's warm-up and first five minutes | UNIT-PLAN rule 6; no opener over ten minutes |
| A teaching day for a multi-part connect id (Cn10, Cn11) uses the same frame or card the item uses | the student meets every part before it is scored |
| A day 4 and day 5 swap (study before practice) keeps each row's school_day, assess and retrieves | only the work moves, not the slot |

## For the structure pass

1. **docs/courses/music-grades-3-to-5/frame.md, Units table "End-of-unit evidence" clauses** (expert 1, for the lead),
   to match the scope's item table. Exact old strings, each once in its unit row:
   - Unit 1 (line 304): "three reasons (interest, knowledge, purpose or setting)" to "one reason per factor (interest,
     knowledge, purpose, setting)"; "how one chosen piece reflects an interest, an experience or a purpose" to "one
     line per part: how one chosen piece reflects interests, experiences and purposes"; "a talk item: one taste,
     piece of knowledge or skill and the music choice it shapes" to "a talk item on the frame "I like ___, I know ___,
     I can ___, so I chose ___""; "a talk item: one tie between an unseen piece and another art, subject or daily
     life" to "a talk item on a four-box card: an unseen piece tied to another art, a school subject, a different
     setting and daily life".
   - Unit 2 (305): "one loudness or speed difference and what each shows" to "one loudness difference and one speed
     difference, each with what it shows".
   - Unit 4 (307): "an unseen four-bar rhythm and short tune read and played" to "an unseen four-bar rhythm and short
     tune, two bars in picture notation and two in standard, read and played"; "one way the song's setting shapes how
     it is sung" to "two lines, how its personal and its social setting each shape how it is sung".
   - Unit 5 (308): "the pick and the reasons, one of them the class's skill" to "one reason per factor (interest,
     knowledge, setting, the class's skill)"; "how one chosen piece reflects a purpose or a context, explained" to
     "one line per part: interests, experiences, purposes and contexts, explained"; the Cn10 and Cn11 talk items as
     unit 1.
   - Unit 6 (309): "a phrase improvised over the drone, with one sentence on its fit to a purpose" to "a phrase
     improvised over a drone note or third the student picks and holds, with one sentence on its fit to purpose and
     setting"; "one tone color choice and what it carries" to "one line each for loudness, speed and tone color, plus
     a talk item on how the student's group used one".
   - Unit 7 (310): "with a sentence on what its sections are for" to "with a sentence on what its sections are for and
     where it would be heard".
   - Unit 8 (311): "one way the piece's cultural setting shapes its performance, explained" to "one line each on how
     the piece's social and cultural setting shape its performance, explained".
   - Unit 9 (312): Pr4.1.5a kept card to "one reason per factor (interest, knowledge, setting, own and others'
     skill)"; Re7.1.5a log page "reflects a context, with one piece of evidence from the music" to "one line per part
     (interests, experiences, purposes, contexts), each with one piece of evidence from the music"; "one way history
     or culture shaped a performance of one of the unit's two works" to "three lines, how history, culture and society
     each shaped a performance of one of the unit's two works, written alone at the start of the supported practice
     day"; Cn10 and Cn11 talk items as unit 1.
   - Unit 10 (313): "a phrase improvised over I and V, with one sentence tying it to a setting" to "a phrase
     improvised over I and V with the student choosing where the chord changes, with one sentence tying it to a
     setting"; "one articulation choice and what it carries" to "one line each for loudness, speed, tone color and
     articulation on a tick-and-word card, plus a talk item on how the student's group used one".
   - Unit 11 (314): "what it is for;" to "what it is for and where it would be heard;".
   - Unit 12 (315): "one way the harmony and the form work in the concert piece, on its marked score" to "the marked
     score scored for timing and pitch, and one way the harmony and the form work in the concert piece".
2. **frame.md, Course-level checks table** (lines 322, 324, 326): "Units 1 and 2 sampled by one written card on two
   unseen readings of one tune, one loudness or speed difference and what it shows" to "Unit 2 sampled by one written
   card on two unseen readings of one tune, one loudness and one speed difference, each with what it shows (unit 1
   was sampled at mid-year)"; "Units 5 and 6 sampled by one written card on an unseen recording, one tone color choice
   and what it carries" to "Unit 6 sampled by one written card on an unseen recording, one line each for loudness,
   speed and tone color and one on the student's own group's use of one (unit 5 was sampled at mid-year)"; "Units 9
   and 10 sampled by one written card on an unseen recording, one articulation choice and what it carries" to "Unit 10
   sampled by one written card on an unseen recording, one line each for loudness, speed, tone color and articulation
   and one on the student's own group's use of one (unit 9 was sampled at mid-year)". Lines 321, 323, 325: after "a
   growth mark" add "; the sample's recording is the second of the two readings".
3. **frame.md, check-day timetable** (expert 5): move the three-minute self-check into the time students wait while
   other groups are at the teacher's spot, so the mid-year written card has nine minutes; or take the unit 1, 5 and 9
   sample down to the setting prompt only. Lead's pick.
4. **scripts/sequence.py** (scope For the lead 1, shared with the other arts band scopes): accept a unit whose next day
   is a `C` Check day whose goal says it stands as that unit's end-of-unit assessment; then `end` moves off days 28,
   46, 92, 110, 156, 174.
5. **docs/courses/CALENDAR.md**: document that a K to 8 band course counts `school_day` across the whole band (lead
   call 5), and regenerate data/plans/calendar.csv with `frame.py calendar` at commit (lead call 8).
6. **Source pass** still owed (scope For the lead 3): the frame's source links and the Claude in Chrome spot-check of
   the grade 3 to 5 words lines (MU:Re7.1, MU:Re9.1, the Pr4.2 c parts).
7. **Defect log**: log the read's findings with `scripts/plan.py defect`, found_by `expert`.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check music-grades-3-to-5`: 0 failures.
- `python -X utf8 scripts/frame.py check music-grades-3-to-5`: 0 failures (unit days 60 a year; 192 days).
- `python -X utf8 scripts/frame.py calendar`: runs; this course's checks stay on weeks 15 and 24 of grades 3, 4 and 5,
  and arts in K to 5 do not count against the stagger, so no break. No frame change was made, so nothing new for the
  regenerated calendar.
- No em dashes in either file; "Curio Class" in full; US spelling.

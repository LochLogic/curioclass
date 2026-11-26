# Expert read: scope and sequence, Media Arts, grades 6 to 8 (2026-11-26)

Course `media-arts-grades-6-to-8`. Brief: docs/pipeline/briefs/sequence-read.md with {subject} = arts, as set by
build/scope-writes/ARTS-READ.md. Cold read: I did not write the scope and sequence or the days.

## What I read

- docs/courses/media-arts-grades-6-to-8/scope-and-sequence.md (whole) and data/plans/media-arts-grades-6-to-8/days.csv
  (all 192 rows, every column).
- The frame, docs/courses/media-arts-grades-6-to-8/frame.md: "The course in brief", the Units table rows and their
  "End-of-unit evidence" lines, "For the lead".
- data/progressions/arts.csv, the ma-g4 to ma-g9 rows (strand, standard ids, assumes).
- data/standards/ncas-performance-standards-words.txt, the 54 grade 6 to 8 media arts lines.
- docs/courses/CALENDAR.md (media arts rows, grades 6 to 8) and data/plans/calendar.csv (every grade 6 to 8 check and
  respond row near school days 78 to 90 and 150 to 160).
- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section 2 (items 1 to 9, "Fails if",
  "Scope and sequence states"), docs/courses/arts/APPROACH.md (works, readiness, critique, how a day opens, pacing),
  docs/courses/arts/STANDARD.md (skimmed for 3.1, 3.2, 3.4), build/scope-writes/ARTS-BRIEF.md.
- Earlier reads on this course: docs/reviews/frame-media-arts-grades-6-to-8-codex-2026-11-25.md and the media arts part
  of docs/reviews/frame-music-theater-media-arts-fixes-2026-11-26.md (to tag repeats and not reopen settled items).

Gates run first: `python -X utf8 scripts/sequence.py check media-arts-grades-6-to-8` 0 failures; `scripts/plan.py check`
reports nothing for this course; `scripts/frame.py calendar` reports no stagger break for it (grade 6 to 8 arts weeks
17 and 32); `scripts/stale.py check` reports nothing for it. I ran my own count: every one of the 54 owned ids sits on
a day of its own year and no id sits in the wrong year. No outside source was opened for this read; the findings rest
on the repo's own standard lines, bar, lens and approach. Per the brief I edited no file but this one, so no
`plan.py defect` rows were logged.

## Verdict

The scope and sequence is sound in its skeleton: the band-year rule is kept exactly, school_day is counted right and
explained, every unit teaches its technique in steps before the making, holds one critique and a revision before its
check, and the course-level checks sit on CALENDAR.md's weeks. It is not ready for unit plans yet: six of the twelve
units have no connecting work at all, two owned ids (MA:Pr6.1.6b, MA:Pr6.1.7b) are scored without a single teaching
day, and several end-of-unit items drop a part of their standard. The one change that matters most is findings 1 and
2 together: a connecting step on an existing work-study day in units 2, 3, 6, 7, 10 and 11, and a taught review of a
trial showing before the year 6 and year 7 screenings.

## Findings, most serious first

### 1. Connecting is missing from six units (2, 3, 6, 7, 10, 11)

LAYER sequence (the frame allows it: "each unit touches at least two"). REPEAT new. Confidence firm.

What is wrong: the unit "Processes" lines and the day notes name no connecting day in units 2, 3, 6, 7, 10 or 11.
Unit 2 lists creating, producing and responding; unit 3 responding, creating and presenting; the same holds a year
and two years later. The lead's read (ARTS-READ.md) and the writer's brief (ARTS-BRIEF.md: "The four processes ...
appear in every unit's days") both ask for all four in every unit.

Why it matters: half the course's units become make-and-judge units with works studied as technique samples only.
The bar's item 7 asks for works taught with their history and setting, and connecting is where that lives. A writer
building unit plans from these rows will not put it in.

Exact fix (no day added, codes unchanged, connecting practiced, not owned): add to the goal or note of one existing
work-study day per unit a two-question setting card (who made it, for whom, where and when, and what it tells us about
that time and place), and name that day as connecting in the unit's "Processes" line:
- unit 2, day 15 (Mafish Fayda, the Frenkel brothers' Cairo studio and its first audience);
- unit 3, day 38 (Tokyo Story, postwar Japan and the family it shows);
- unit 6, day 84 (Jáaji Approx., language and family, under the flag already in the note);
- unit 7, day 102 (Two, Calcutta in 1964, a rich boy and a poor boy);
- unit 10, day 148 (Pumzi, a Kenyan team making science fiction on a small budget);
- unit 11, day 166 (Song of the Sea, Irish folklore and early Irish art).

### 2. MA:Pr6.1.6b and MA:Pr6.1.7b are scored but never taught

LAYER sequence. REPEAT new. Confidence firm.

What is wrong: my count of teaching days per code (every row that is not Check or Respond) gives MA:Pr6.1.6b and
MA:Pr6.1.7b zero teaching days. Each appears first on the second check day (61, 125) as a written item ("how the
screening went and one improvement, with evidence from the audience"; "results, one improvement and growth since unit
4"). Year 8 does it right: day 186 (trial showing with feedback) and day 187 (counted revision) teach MA:Pr6.1.8b
before day 189 scores it.

Why it matters: students are scored on analyzing a presentation they were never shown how to analyze. The approach
page's "no opening task asks for a technique not yet taught" and the lens's "a making task with no technique taught
first" both apply.

Exact fix: on day 57 (and day 121), after the trial showing in pairs, add the review frame: each pair writes how the
trial went and one improvement, with one piece of audience evidence (day 121 adds "and what I can do now that I could
not in unit 4"); add MA:Pr6.1.6b (MA:Pr6.1.7b) to the day's codes. On day 58 (day 122) the revision names the
improvement from that review. No day added.

### 3. End-of-unit items drop parts of their standards

LAYER sequence. REPEAT yes (the C-68 frame read found Re9 context dropped from the evidence, the same kind). Confidence
firm for the first two bullets, likely for the third.

What is wrong (APPROACH: "Every part has an end-of-unit item"):
- MA:Re7.1.6b and MA:Re7.1.7b name "techniques and styles". The day 13 and day 77 items, and the mid-year checks on days
  33 and 97, ask for "one technique" only. Style is never asked in years 6 and 7.
- MA:Cn11.1.8b names legal, technological and virtual-world settings. Day 135 teaches two case cards (a virtual world,
  a shared-image tool), but the day 141 evidence is "license lines and one case card", so a student meets only one of
  the two non-legal settings.
- MA:Cn11.1.6a names identity, history, entertainment and community; MA:Cn11.1.8a civic, environmental and community
  values. Each is scored only on a piece that shows one tie or one value the student chose. The works cover the
  range, the evidence does not.

Why it matters: a student can be marked met on an id while a named part was never asked, and a unit plan writer will
copy the item as written.

Exact fix: day 13, 33, 77 and 97 items read "one technique and one style"; the kept media-ethics card scored on day
141 holds a line for each of the two case cards; the kept investigation piece (day 12) and values piece (day 140) each
carry a three-line card naming how a studied work shows each of the other ties or values, scored with the piece.

### 4. The screening units do not say who makes the piece, and the evidence does not hold either way

LAYER sequence (frame silent). REPEAT yes (frame read M3: a team piece standing in for one student's evidence). Confidence
likely.

What is wrong: units 4, 8 and 12 never say whether the 60-to-90-second piece is a student's own or a team's. Day 57
runs "a trial showing in pairs", which reads as one piece each; day 60 runs "five teams of six screen in turn ...
about five minutes each". If the pieces are each student's own, 30 pieces of 60 to 90 seconds need 30 to 45 minutes,
not 25. If they are team pieces, MA:Pr4.1.6, 7 and 8 ("every form backs the core message") is marked per student from
a team piece, which the course's own rule ("a team piece never stands in for one student") forbids for the production
ids and the same logic forbids here.

Exact fix: state on days 55, 119 and 183 that the piece is made in pairs, 60 seconds, each partner owning one half and
its forms; each student fills a one-line card "how my half's forms back the message", kept and scored with the piece
for Pr4. Day 60, 124 and 188 notes then read: 15 pair pieces of about a minute with turnover, 25 minutes, the teacher
marking each student's presenting task and Pr4 look-for on their own half.

### 5. On the once-a-week path, session 1 of each screening unit holds seven days

LAYER frame (the 7, 9, 6, 6 split and the six-session screening sequence are the frame's). REPEAT new (the C-68 read
fixed assessment in respond, not this load). Confidence likely.

What is wrong: session 1 of units 4, 8 and 12 merges days 49 to 55 (two works, one with a sensitivity flag, the
source-log demonstration, the technique demonstration, its drill, the research and the start of the draft) into 40
minutes. The screening unit has three teaching sessions for eleven teaching days, while unit 2 has seven for sixteen.
Unit 3's session 1 (days 35 to 38: two works, the angle demonstration and its drill) is heavy too.

Why it matters: the path keeps every id in name, but a teacher cannot teach Bey's work with its flag and a new
technique in the same few minutes; the screening's Pr4 and Cn10 evidence then rests on untaught steps.

Exact fix, for the lead (frame change): units of 7, 8, 6 and 7 sessions. Unit 2 merges days 28 to 30 (revision, the
30-second screening of five team pieces, records) into one session, keeping critique and revision in separate
sessions. Unit 4 gets: 1, days 49 to 51 (works and the source log); 2, days 52 to 55 (technique, research, draft); then
the frame's sessions 2 to 6 as written. Week placement of the checks does not change.

### 6. Works lean to one century, and digital or interactive media is absent

LAYER frame. REPEAT new. Confidence judgment call.

What is wrong: year 7 studies eight works, seven made between 1910 and 1964 (Hopinka, 2015, is the one later work).
Across the band, 3 of 27 works are from after 2010 and none is interactive (a game, a web or app piece, a virtual
world). Cn11.1.8b's virtual-world setting is met only through invented case cards. The writer flagged the year 7
living-maker gap (For the lead item 3); the period gap is wider than that.

Why it matters: the lens names "works all from one century" as an error, and APPROACH warns that open sources lean old.
An adoption reviewer in media arts would expect some contemporary and interactive forms. The cost is low, since a
work may be described and linked, never embedded.

Exact fix, for the lead: when the unit plans confirm works (frame For the lead item 6), let the unit 7 and unit 12
Candidate picks be post-2000 makers, and swap one of the two unit 8 science works (Smith 1910 or Edgerton 1957) for a
contemporary science-visualization or interactive explainer, described and linked. No day changes.

### 7. Smaller items, settled in the table below

- Day load: day 2 holds the retrieval task, the shot-size demonstration and the Starevich study in about 20 working
  minutes; day 130 holds the retrieval, the style step card and the Earthrise contrast. Days 12, 76 and 140 each hold
  a revision, an extra task and the class showing. LAYER sequence, REPEAT new, likely.
- 10-days-short: on days 54, 118 and 182 the folded baseline look lands on research days where the look-for (forms
  backing a message) cannot be seen. LAYER sequence, REPEAT new, firm.
- Once-a-week path: fluency days fold into openers, but the path never says where the baseline look goes. LAYER
  sequence, REPEAT new, firm.
- Stale notes: days 63, 127 and 191 say "samples units 1 to 3" (5 to 7, 9 to 11); the codes and the .md table say units
  2 and 3. The .md's reason for leaving Re9 unsampled ("needs the class's own pieces") contradicts day 40, which
  teaches Re9 on a Curio Class example piece; the real reason is the frame's two-task cap. The year 7 "Works range"
  line lists France twice. LAYER sequence, REPEAT new, firm.
- Day 168 plans the style piece "through the workflow" from unit 10 with no recall of the workflow chart. LAYER
  sequence, REPEAT new, likely.

## What is right and should not be touched

- The band-year rule: 18 ids a year, each year's heading naming its grade, every id on a day of its own year, never a
  claim on the year before's ids.
- school_day: 2.5 x the day in the year, rounded up, year 7 + 160 and year 8 + 320, explained in the .md; checks on
  school days 83 and 158, matching CALENDAR.md and calendar.csv, off every core check day in grades 6 to 8.
- Retrieval mapping matches the progression's "assumes" column exactly (each unit retrieves its two threads one grade
  back on day 2); no readiness check is needed and day 1 stays clean in every unit.
- Technique days come before making in every unit, techniques get harder year to year (shot sizes, long take and
  cut, style conventions; flip book, animatic, found-sound layer), and each unit has one critique on its second
  making day and a revision before the check.
- Production ids scored from each student's kept trials over three sessions, ten students a session.
- Course-level checks draw from earlier units and say so; the 13 unsampled ids a year are named with reasons.
- The paper path, the safety lines and the sensitivity flags in the notes (Reel Injun's stereotype clips described,
  never screened; Vertov's excerpts named; Bey with no image of the bombing).
- The logic model on one page.

## What I could not judge

- Whether each work's excerpt passes the flash rule and whether the dates and holding pages are right (frame For the
  lead item 6; the unit plans open each page).
- Whether 12 to 13 minutes is enough for "a fresh plan with a mockup" on the year-end checks; a trial sitting would
  tell.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Move Starevich's The Grasshopper and the Ant from day 2 to day 1, beside the Lumière film (fixed frame against staged scene); day 2 keeps the retrieval and the shot-size step card; Re7.1.6b added to day 1's codes | Day 2 cannot hold a retrieval, a demonstration and a work study in 20 working minutes; day 1 has no retrieval and both films are short | data/plans/media-arts-grades-6-to-8/days.csv, scope-and-sequence.md unit 1 |
| Move the Earthrise contrast from day 130 to day 131; the drill's stills include Earthrise and the Parks portrait | Same load reason; the drill then practices on the pair | days.csv, .md unit 9 |
| Day 76's "finish each student's own lines of the class rules" moves to day 72's drill; day 140's case-card analysis moves to day 136's drill; on days 12, 76 and 140 the showing runs as a pair gallery walk | Revision plus showing fits 30 minutes only without the extra task | days.csv, .md units 1, 5, 9 |
| On the 10-days-short year the folded baseline look moves to day 55, 119 and 183 (making), not 54, 118 and 182 (research) | The look-for is about blended forms, seen only while making | .md Shorter path table, days.csv notes on 53, 117, 181 |
| Once-a-week path: the baseline look runs in the session that holds the folded fluency opener | The path must still give two marks a unit | .md Shorter path |
| Days 63, 127 and 191 notes read "samples units 2 and 3" (6 and 7, 10 and 11) | Matches the codes and the .md table | days.csv |
| The .md's reason for not sampling Re9.1.g on a check reads "the frame cuts each check to two tasks" | The stated reason contradicts day 40 | .md Course-level checks |
| Day 168 opens with a five-minute recall of the unit 10 workflow chart | Practice that returns, used earlier the same year | days.csv |
| Year 7 "Works range" line lists each country once | Copy fix | .md |

## For Cory

None new. The scope, money and people questions already on the frame (supplies ceiling, a shared device per team for
the technical-quality id) are unchanged by this read.

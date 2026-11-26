# Expert read: scope and sequence of music-grades-k-to-2 (2026-11-26)

Cold read, curriculum expert role (docs/agents/EXPERT.md), brief docs/pipeline/briefs/sequence-read.md with the arts
notes in build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write the scope and sequence or the frame.

## What I read

- docs/courses/music-grades-k-to-2/scope-and-sequence.md and data/plans/music-grades-k-to-2/days.csv (192 rows), in full.
- docs/courses/music-grades-k-to-2/frame.md, in full (Units table, Seams, Models carried, Course-level checks, Cross-subject, For the lead).
- The lens docs/agents/lenses/arts.md; the bar, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9, "Fails if", "Scope and sequence states"); docs/courses/arts/STANDARD.md section 3; docs/courses/arts/APPROACH.md, in full.
- build/scope-writes/ARTS-BRIEF.md; docs/pipeline/briefs/sequence-write.md rules 2, 3 and 10.
- The music rows mu-k-*, mu-g1-*, mu-g2-* (and mu-g3-* for the hand-on) in data/progressions/arts.csv; the 59 K to 2 lines in data/standards/ncas-performance-standards-words.txt.
- docs/courses/CALENDAR.md (music K to 2 rows) and the course's rows in data/plans/calendar.csv.
- Gates: `scripts/sequence.py check music-grades-k-to-2` 0 failures; `scripts/frame.py calendar` 0 failures for this course (unit days K 60, 1 60, 2 60); `scripts/plan.py check` reports failures only in other courses (algebra-ii), none here; `scripts/stale.py check` 121 files, 0 failures.
- A script over days.csv: every one of the 59 owned ids sits on days of its own year only, none missing, none extra; each id's teaching, practice and check days were listed (used below).

## Verdict

The scope and sequence is sound: it keeps the frame's units, days and checks exactly, places every one of the 59 ids in its own year, puts every technique before the making that uses it, and gives every unit a critique, a revision and a showing before its end-of-unit assessment, with both shorter paths holding. The biggest risk is in the checks: day 37 assesses MU:Pr4.3.Ka on loudness alone while the .md says voice quality, loudness and speed are each prompted, and several two-part items ask "louder or faster", so a busy item writer will build items that miss parts of the code. The one change that matters most is to give every check row a prompt for each part it claims (day 37 first), then fix unit 9's crowded day 142 and the rhythm syllables the frame starts in unit 1 that no day teaches. There are 11 findings; none needs Cory.

## Findings, most serious first

### 1. Check prompts do not cover each part of MU:Pr4.3.Ka, MU:Re8.1.Ka and MU:Re8.1.1a (LAYER sequence, REPEAT yes)

**What is wrong.** The .md (unit 2 Assessments) says the day 37 performance item has "voice quality, loudness and speed each prompted". The day 37 row only has the group sing "soft then loud". Speed is never prompted, and voice quality is never taught apart from loudness: day 20's note says "Voice quality is one part of the code", but its goal teaches a soft voice and a strong voice, which is loudness again. The talk item for MU:Re8.1.Ka (day 37) asks "where it gets louder or faster", and MU:Re8.1.1a (day 97) asks about "the loudness or speed choice". Both codes name loudness and speed, so a child who answers only one has been marked on half the code.

**Why it matters.** sequence-write rule 2 ("each part of each code") asks for a prompt per part. The unit plan writer copies the check row, not the .md summary, and will build a one-part item.

**Fix (no day added).** Day 20 teaches voice quality as its own step: the whisper, speaking and singing voices (leaving out the calling voice because of the no-shouting rule), then sings one class song soft and strong. Day 22's drill echoes all three. Day 37's performance item becomes three prompts: the group sings soft then loud, then slow then fast, then in a whispered and a singing voice, and each child points to the picture of the way that fits the words for each. Day 37's MU:Re8.1.Ka item uses an unseen Curio Class original that gets louder at one point and faster at another, and the child shows each change. Day 97's MU:Re8.1.1a item names both choices, the loudness choice and the speed choice. Change the .md unit 2 line to match.

**Evidence and confidence.** The words-file lines for the three ids; sequence-write rule 2. Firm. Teaching voice quality through whisper, speaking and singing voices is common K to 2 general music practice (from memory). Note for the lead: from memory, the 2014 handout gives Pr4.3.Ka's three qualities as "such as" examples, and the words file has dropped the "such as". If the lead restores it, voice quality becomes optional, but loudness and speed stay prompted because both MU:Re8.1 lines name them without examples.

### 2. Unit 9: day 142 holds revision, a partner-class showing and a two-piece listening log in 40 minutes (LAYER sequence, REPEAT new)

**What is wrong.** Unit 9 has three application days (139, 141, 142) against unit 5's five. The critique is on day 141, and day 142 then has to fit the revision, the showing of "Arirang" to a partner class, and the kept MU:Re9.1.2a log page, which needs two unseen pieces played and judged. That leaves about 29 minutes once set-up, clean-up and the opener are taken out. Meanwhile day 140 is a fluency day sitting between the first application day and the critique.

**Why it matters.** Either the revision or the kept log page gets rushed, and the log page is scored evidence. Unit 5's day 78 (showing plus log page) is also tight, but it carries no revision, so it can stand.

**Fix (a day swap inside the unit, settled below).** Day 140 becomes the critique (Application, the unit's second application day), and its reading and conducting drill moves into the openers of days 140 and 141. Day 141 becomes the revision, and day 142 the showing and the kept log page. On the once-a-week path, unit 9's sessions become 129-132, 133-135, 136-137, 138-139, 140, 141-142, 143, 144 (still 8). In the year 2 fold-in list, day 140 is replaced by day 175 (unit 11's read-back drill once finding 8 is applied, or day 174 if it is not).

**Confidence.** Likely (minute arithmetic from the .md's own day budget).

### 3. Unit 9 performs songs of only one culture for MU:Pr4.2.2a (LAYER sequence, REPEAT new)

**What is wrong.** The words line asks for tonality and meter shown "across music of many cultures chosen for performance", and the frame's row says "Arirang and one other". In days.csv the class performs only "Arirang" (days 136, 139 to 142). "Tumbalalaika" (day 137) is played as a recording or sung by the teacher, and Joplin is listened to.

**Why it matters.** The "many cultures chosen for performance" part is carried only by listening, which is MU:Re7.2's work, not Pr4.2's.

**Fix (no day added, settled below).** Day 137: the class sings the "Tumbalalaika" refrain from the read-aloud guide and conducts it in threes, then hears the verse. This puts two cultures' songs in minor-or-major and twos-or-threes in the children's voices. The day 137 note keeps the sensitivity line (a secular riddle song, a Jewish music archive's page read first, no costume, no accents). If the sensitivity read rules against children singing it, day 139's accompaniment runs on a year 1 class song from another culture instead ("Sakura Sakura"), sung and conducted.

**Confidence.** Likely.

### 4. The rhythm-syllables model the frame starts in unit 1 is on no day of year K (LAYER sequence, REPEAT new)

**What is wrong.** The frame's Models carried table says rhythm-syllables is introduced in unit 1: "ta" and "ti-ti" spoken with the patted beat, by ear, with no symbols. It is also mu-k-read's model_out in the progression. No day from 1 to 64 says "ta" or "ti-ti". So year 1's day 67 introduces the syllables and the picture symbols for them on the same day, and day 66's retrieval of mu-k-read cannot retrieve them.

**Why it matters.** Sound before symbol is the order the frame chose. Without it, day 67 carries two new things for a grade 1 child, and the model handed to grade 3 has a gap at its start.

**Fix (no day added, settled below).** Day 9's echo drills add "ta" spoken on each patted beat, echoed after the teacher. Day 13's echo drill adds "ti-ti" for two even sounds on one beat, by ear only, with no symbols and nothing scored. Day 66's retrieval opener adds an echo of "ta" and "ti-ti" patterns before the picture cards.

**Confidence.** Firm (frame table and the progression's model_out against days.csv).

### 5. Retrieval missing where a unit builds on an earlier unit's row (LAYER sequence, REPEAT yes)

**What is wrong.** Unit 9 teaches meter by conducting (day 130) and tonality by reference patterns (day 131). Both rest on unit 7's twos and threes and major and minor (mu-g1-invent, days 101 to 105), which is a year-before row. Unit 9 retrieves only mu-g1-read and mu-g1-respond. Inside a year, the .md's own "Why this order" says unit 3's motifs are made from unit 1's high and low and unit 2's loud and soft, and that unit 10's explanation of a pick uses unit 9's named tonality and meter. Neither unit retrieves those rows, although units 4, 7, 8, 11 and 12 do retrieve the same-year rows they build on.

**Why it matters.** A grade 2 child last sang major and minor reference patterns about 22 school weeks earlier, across a summer. Rule 2 asks for retrieval inside a day, and the course applies that rule unevenly.

**Fix (no day added, settled below).** Day 131's opener (10 minutes) retrieves unit 7's major and minor reference patterns and twos and threes pats (`retrieves`: mu-g1-invent). Day 41's opener retrieves high and low and loud and soft shown with the body (`retrieves`: mu-k-read; mu-k-express). Day 153's opener retrieves conducting twos and threes and the major and minor cards (`retrieves`: mu-g2-read). Add the three lines to the .md's Readiness and retrieval paragraph.

**Confidence.** Firm for unit 9 (it is a year-before row), likely for units 3 and 10 (by the writer's own stated dependencies).

### 6. MU:Cn11.1 and MU:Cn10.1.Ka parts are not all carried by days (LAYER sequence, REPEAT yes)

**What is wrong.** MU:Cn11.1's words line names four parts: other arts, school subjects, different settings and daily life. In year K, day 7 uses story, game and time-of-day cards, and day 11 gives the playground setting, but no year K day ties music to a school subject. Year 1 (day 73) and year 2 (days 136 and 137: a map, a dance) cover all four. MU:Cn10.1.Ka names tastes, knowledge and skills. Day 29 and the day 37 look-for use "what the child likes or knows", and "what the child can do" appears only in years 1 and 2.

**Why it matters.** Each year claims its own id in full (STANDARD.md 3.1), so year K owes every part.

**Fix (no day added, settled below).** Day 7's card set adds a school-subject card (a counting song) and a place card, so the four parts are each taught. The day 17 talk item keeps one talk item, drawn from a card set with one card for each part. Day 29's model adds "because we can clap it" beside "because I like it" and "because I know it", and day 37's look-for accepts any of the three. Whether a single connecting talk item is enough for a four-part line, given the two-talk-item cap, is a judgment call; I would keep one item and rely on the days to carry all four parts.

**Confidence.** Likely for the days; judgment call for the item.

### 7. Check-day minutes are thin for the creating checks (LAYER frame, REPEAT new)

**What is wrong.** Every check day gives each group of five about four minutes, roughly 48 seconds a child. On day 113 (year 1 year-end), each child improvises a reply, plays two short ideas over the teacher's accompaniment, and answers two talk items. On day 177 (year 2 year-end), each child improvises a rhythm pattern and a melody pattern, plays two patterns in a given meter and tonality, and answers two talk items. That is four or five performances and answers in under a minute, with no room for a seven-year-old's pause. Days 37 and 97 also need their unseen pieces and the menu of three songs played: if that happens once per group, it eats the four minutes.

**Why it matters.** A teacher who runs over loses the last group, and their marks fall to the respond day, which is meant to start from the marks.

**Fix (for the lead, frame layer; the scope cannot fix it alone).** (a) The scope and sequence states that each check's unseen pieces and menu songs are played once to the whole class in the spare four minutes before the groups (frame budget: 36 of 40 minutes). (b) The frame lets a group not reached by the end of the check day take its turn in the first ten minutes of the respond day, before the "not yet" groups form, and names this in the respond row. Neither adds a day.

**Confidence.** Likely (arithmetic from the frame's own budget). It needs a try in a real room.

### 8. Units 7 and 11 put a fluency day between the critique and the revision (LAYER sequence, REPEAT new)

**What is wrong.** Unit 7 runs critique on day 109, a drill on day 110 and the revision on day 111. Unit 11 runs critique on day 173, a drill on day 174 and the revision on day 175. The frame's Day kinds say "the next day's revision", and APPROACH "Critique" has students revise after the feedback. At two sessions a week, the gap is a full school week (school days 273 to 278 and 433 to 438).

**Why it matters.** Kindergarten to grade 2 children forget a spoken suggestion across a week. The other ten units put the revision on the next session.

**Fix (a day swap inside the unit, settled below).** Swap days 110 and 111, and swap days 174 and 175. Kinds and codes move with the rows, and each unit's arc line in the .md follows.

**Confidence.** Likely.

### 9. Two responding ids get a single teaching day and no practice before they are scored (LAYER sequence, REPEAT new)

**What is wrong.** MU:Re9.1.Ka is on day 10 only, then scored on day 17 (and sampled again on day 49). MU:Re7.1.2a is on day 154 only, then scored on day 161. Every performing id in the band has four to nine days.

**Why it matters.** "Days by load" in the read brief: a responding id taught once is scored on a first exposure plus a week.

**Fix (no day added, settled below).** Day 16's partner line becomes "I like it because it is ___" with a sound word (MU:Re9.1.Ka added to codes). Day 160's log page asks the child to add one interest or experience to the reason (MU:Re7.1.2a added to codes). The scored kept work on day 160 stays MU:Pr4.1.2a and MU:Cn10.1.2a, and MU:Re7.1.2a stays a talk item on day 161.

**Confidence.** Likely.

### 10. The composed works span 1781 to 1932, plus one work from 1972 (LAYER sequence, REPEAT new)

**What is wrong.** The range across cultures is good: Africa, Asia, Native American makers, Latin America, Europe, and living makers in each year. The composed concert works, though, are all from Mozart (about 1781) to Price (1932), with Reich (1972) after. Nothing comes before the classical period. The lens's error is "all from one century", which this course does not commit, but bar item 7 asks for "many times", and an adoption reviewer would note the narrow window.

**Fix (lead's choice, 0 days).** Add one earlier work as a short listen inside a day that already exists. A good fit is Vivaldi's "Spring" from The Four Seasons (1725) beside "Sakura Sakura" and the spring picture on day 73 (MU:Cn11.1.1a), with a public domain score and its recording's rights line checked. This is taste as much as bar, so I did not settle it.

**Confidence.** Judgment call.

### 11. Small accuracy and process notes (LAYER sequence and process, REPEAT new)

- **Labels.** The .md's Course-level checks table labels the year-end samples "Units 1 and 2", "Units 5 and 6" and "Units 9 and 10", but each samples one unit's id (MU:Re9.1.Ka, MU:Re9.1.1a and MU:Re7.2.2a belong to units 1, 5 and 9). The wording comes from the frame. Fix: name the one unit in the .md table and the three check rows' notes.
- **`end` on Application days** (For the lead item 1). Days 36, 48, 96, 112, 160 and 176 carry `assess` = `end` on supported practice days so the gate passes. The notes say plainly that this is part 1 of an assessment taken on the check day, so a writer will not misread them. I agree with the writer's ask: let scripts/sequence.py accept a check day that the frame names as a unit's end-of-unit assessment, then remove the marks. Process; nothing to change in this course yet.
- **Stale formatting outside this course.** docs/courses/CALENDAR.md's music K to 2 rows (lines 71, 86, 101) read "week 19 week 19, Year K year-end (week 25 week 25". The weeks are right, but the generated cell is garbled, as it is for every arts row there. Process, for whoever owns the calendar generator.

## What is right and should not be touched

- **Year placement.** Each year's ids are on its own days only (script check: 0 wrong-year codes, 59 of 59 present). The id count per year (19, 20, 20) and the mixed-class note are stated once at the top, as the bar's "Scope and sequence states" asks.
- **Unit shape.** Every unit gives the listen first, then a technique taught with a step card before any making, a fluency day carrying the baseline look, the critique on the second application day, a revision, a showing, the check and a respond day. Every showing has its critique and revision before the end-of-unit assessment.
- **The four processes.** All four are named on days in every unit. Creating in the reading units is marked "practiced, not claimed", which is honest.
- **Calendar.** school_day follows ceiling(5n / 2) and is stated. All six course-level checks sit on CALENDAR.md's weeks (K 19 and 25; years 1 and 2 17 and 25) and match calendar.csv. The concert units' check days fall in week 32, after the core year-end weeks, which is right for specials.
- **Rule 3 coverage.** The 26 codes not sampled on a course-level check are named, with the reason (the after-core design and the K to 2 weeks 29 to 32 rule). That satisfies L107 as written.
- **Shorter paths.** The once-a-week table gives 32 sessions a year, matches the frame's 9, 9, 4, 6 and 8, 8, 6, 6, keeps every critique, revision, kept-work day and respond day in its own or a merged session, and keeps the check weeks. The ten fold-in days a year are all unassessed fluency days.
- **Safety and sensitivity.** Every flagged work names its flag and the source the agent reads first. Day 179 carries the hard-history flag on the juba, with no imitation. The tuned bottles are plastic. No headphones, no solo singing, no sacred work.
- **Math and PE boundaries.** No note values anywhere, math bridges on days 2, 101 and 130, and the PE boundary named on moving days.

## What I could not judge

- Whether the four-minute group turns work with real kindergartners (finding 7). It needs one tried check day.
- The rights lines and current status of the living and recent makers. These are the unit plans' job.
- Whether "Kye Kye Kule" is a game song with a reliable Ghanaian attribution, since published accounts differ (from memory). The frame already sends this to the sensitivity read.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 20 teaches the whisper, speaking and singing voices as voice quality, then soft and strong; day 22's drill echoes all three | Voice quality is claimed but never taught apart from loudness | days.csv days 20, 22; .md unit 2 arc |
| Day 37's MU:Pr4.3.Ka item prompts loudness, speed and voice quality, each pointed to; the MU:Re8.1.Ka original changes in loudness and in speed at different points, and each is shown | A prompt per part (rule 2) | days.csv day 37; .md unit 2 Assessments |
| Day 97's MU:Re8.1.1a talk item names the loudness choice and the speed choice | A prompt per part | days.csv day 97 |
| Unit 9: day 140 becomes the critique (Application), day 141 the revision, day 142 the showing and the kept log page; day 140's drill moves into the openers of days 140 and 141 | Day 142 was overloaded; this keeps the critique on the second application day | days.csv days 140 to 142; .md unit 9 arc, once-a-week row, year 2 fold-in list (replace 140 with 175, or 174 if the unit 11 swap is not applied) |
| Day 137: the class sings the "Tumbalalaika" refrain and conducts it in threes (fallback: "Sakura Sakura" on day 139) | MU:Pr4.2.2a asks for performed music of more than one culture | days.csv day 137 |
| "ta" on day 9 and "ti-ti" on day 13, by ear and echoed, not scored; day 66's retrieval echoes both | The frame's rhythm-syllables model starts in unit 1 | days.csv days 9, 13, 66 |
| Retrieval openers: day 131 (mu-g1-invent), day 41 (mu-k-read; mu-k-express), day 153 (mu-g2-read) | Rule 2, for rows the unit builds on | days.csv `retrieves` and notes; .md Readiness paragraph |
| Day 7 adds a school-subject card and a place card; the day 17 card set has one card per MU:Cn11.1 part; day 29 adds "because we can ___" (skills), accepted on day 37's look-for | Year K carries every part of MU:Cn11.1.Ka and MU:Cn10.1.Ka | days.csv days 7, 17, 29, 37 |
| Swap days 110 and 111; swap days 174 and 175 | The revision comes the session after the critique | days.csv; .md unit 7 and unit 11 arcs; fold-in list if 174 or 175 is named |
| MU:Re9.1.Ka added to day 16's partner line; MU:Re7.1.2a added to day 160's log reason | Practice before scoring for ids taught once | days.csv days 16, 160 |
| The .md check table names the one unit sampled on each year-end check | Accuracy | .md Course-level checks |

## For Cory

Nothing. Every finding stays inside the standards and the frame's scope. Finding 7 (check-day minutes) and finding 10 (an earlier work) are the lead's calls.

## Sources

- data/standards/ncas-performance-standards-words.txt: the 59 lines, for the part-by-part check.
- data/progressions/arts.csv: the rows' standards, `assumes` and model_out, for findings 4 and 5.
- docs/courses/music-grades-k-to-2/frame.md: Models carried, Day kinds, check budget.
- docs/courses/arts/APPROACH.md "Critique" and "Kinds of day"; docs/agents/lenses/arts.md error list.
- From memory, not opened for this read: the 2014 NCAS handout's "such as" wording for MU:Pr4.3.Ka; the whisper, speaking and singing voices as a K to 2 voice-quality step; the dates of the Vivaldi work. Nothing from outside the repository was opened, so there is nothing new for the source list.

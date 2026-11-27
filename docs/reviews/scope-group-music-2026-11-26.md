# Scope group read: music, K to 12 (2026-11-26)

The four music scopes read side by side, through the grades: music-grades-k-to-2, music-grades-3-to-5,
music-grades-6-to-8, music-grades-9-to-12. This read looks only at what no single-course read could see. The four
sequence reads and their fix passes (docs/reviews/sequence-music-grades-*-2026-11-26.md and -fixes-2026-11-26.md)
are not repeated, except where a fix made the group worse (finding 6).

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/ARTS-BRIEF.md;
  docs/agents/lenses/arts.md; docs/ADOPTION-BAR-SUBJECTS.md section 2; docs/courses/arts/STANDARD.md (sections 3
  and 5) and APPROACH.md ("Works and their settings", "Family note", the student-life rules).
- The 100 music rows of data/progressions/arts.csv (strand `mu`, K to 12).
- For each course: frame.md (Seams, Models carried, Units, the technique ladder in 9 to 12), scope-and-sequence.md
  in full, and data/plans/<course>/days.csv read with short Python scripts (works named, syllable and solfege words,
  critique wording, safety and sensitivity lines, owned codes against taught and assessed days, Cn10 days).
- The four sequence reads and fix reports (searched for what each settled).
- docs/courses/CALENDAR.md (rules 1 to 5, target weeks, the generated table), data/plans/calendar.csv for music,
  `scripts/frame.py calendar` (no break) and `scripts/sequence.py check` on all four (0 failures; 9 to 12 prints
  the expected "standard None" notes for Level 4).
- DESK-ANSWERS.md: the 2026-11-26 arts scope lead calls, the after-core frame calls and the computer science scope
  lead calls (for the sequence.py change in finding 8).

## Findings

### 1. Key signatures are taught on no day of the group, though 6 to 8 uses them and 9 to 12 promises them

- **Courses and days.** Music 6 to 8 day 131 (grade 8) sight-reads in four steps, the first "key and meter"; day 2
  names sharps and flats as single symbols, and no grade 6 to 8 day teaches what a key signature is or how to find
  the home note from it. Music 9 to 12 frame, "Techniques that get harder": "major keys to three sharps and flats"
  (Level 1) and "all key signatures" (Level 2). No Level 1 or Level 2 day carries either: day 6 teaches solfege on a
  major scale, days 35, 189 and 349 drill notation "checked against the key", day 175 teaches minor keys.
- **Why it matters.** A step that names a key the student was never taught to read fails the lens line "technique is
  taught, not hoped for", and Level 1's notation drills and Level 2's minor keys both rest on it. A unit writer
  building from these days will not write the lesson, since no day asks for it.
- **Fix.** Music 9 to 12 day 6: "Solfege on a major scale, and major key signatures to three sharps and flats
  (finding do from the signature), with the step card"; day 175 adds "relative minor and all key signatures on the
  circle of keys". Music 6 to 8 day 131's goal names the first step as "key (the key signature of G or F, from day 2's
  sharp and flat) and meter", taught on that day's step card for the two keys its lines use.
- **Tag: scope.**

### 2. Music 6 to 8: MU:Pr4.1.6a, 7a and 8a are scored on no assessed day

- **Courses and days.** In music 6 to 8 the kept performance program (MU:Pr4.1.6a) is finished on day 35, an
  Application day with a blank `assess`; the showing day 34 (Check, end) carries only MU:Pr4.3.6a, and the
  mid-year check day 37 lists MU:Re8.1.6a, MU:Re7.1.6a, MU:Cn10.1.6a and MU:Pr4.2.6b but not MU:Pr4.1.6a. The same
  holds for days 99 and 101 (7a) and 163 and 165 (8a). The scope's check table says "MU:Pr4.1.6a from day 35", but
  days.csv records the code on no assessment. Music K to 2 and 3 to 5 solved the same design (kept work scored with
  the check) by marking the kept-work day; 6 to 8 marked the showing instead and left the kept page out.
- **Why it matters.** Three owned ids show as taught but never assessed in the day record, which is what the
  ledger, the unit plans and the end-of-course read count from.
- **Fix.** Add MU:Pr4.1.6a, 7a and 8a to the codes of days 37, 101 and 165, with the goal's existing "carries the
  unit's record" wording naming the kept program page from days 35, 99 and 163, scored once.
- **Tag: scope.**

### 3. The pitch and rhythm syllable systems are never named, and solfege breaks off between grade 3 and Level 1

- **Courses and days.** Music K to 2 names "ta" and "ti-ti" (days 9, 13, 67) and on day 133 adds a rest "counted by
  beats and a spoken counting system" without saying which; it reads so, mi and la on a staff (day 134). Music 3 to 5
  uses "syllables and beat counts" (days 3, 33) and a pentatonic call and answer (day 18), then from year 4 reads
  tunes "by letter names on the treble staff" (days 117, 178). Music 6 to 8 reads by letter names and uses "rhythm on
  syllables" (day 131) with no syllable named, and no solfege day. Music 9 to 12 day 6 teaches "solfege on a major
  scale" as new, and day 4 reads sixteenths "with rhythm syllables" with none named. The rhythm-syllables model is
  carried in all four frames' Models carried tables, but only K to 2 says what the syllables are.
- **Why it matters.** A model carried by name through 13 grades means a different thing in each course: a teacher
  in grade 4 does not know what grade 2 said, and a student who sang so, mi and la in grade 2 meets solfege again
  only in Level 1, five grades later, as if new. This is the drift the lens warns of (a K to 2 skill that does not
  grow), and it is invisible inside any one course.
- **Fix.** State the two systems once, in each frame's Models carried row for rhythm-syllables, word for word:
  rhythm by "ta", "ti-ti", "ta-a" and the rest, with "ti-ka-ti-ka" for sixteenths, beside beat numbers from grade 3;
  pitch by movable do with la-based minor, growing from so, mi, la (K to 2) to the pentatonic (grade 3) and the full
  major scale (grade 4), and kept beside letter names from grade 4 on. Then in the days: K to 2 day 133 names the
  counting system; 3 to 5 days 117 and 178 read "by letter names and solfege"; 6 to 8 day 131's second step reads
  "rhythm on the ta and ti-ti syllables" and its fourth sings the line in solfege; 9 to 12 day 6 becomes a revisit
  for a student from 6 to 8 ("a named revisit") and stays new for a student without it. My pick is movable do and
  this rhythm set because both are the ones most open early-grade material uses and they need no purchase; the
  lens leaves voice pedagogy at depth to a qualified music teacher, so the frame line may say the school may swap
  in its own system as long as it keeps one through the band.
- **Tag: frame** (the frame rows carry the rule; the day wording follows in the scope fix).

### 4. The claim and evidence card is worded four ways, and grade 8 teaches as new what grade 5 already taught

- **Courses and days.** Music 3 to 5 day 132 (grade 5): "a claim, two pieces of evidence from the music, a link".
  Music 6 to 8 day 137 (grade 8): "the short form: a claim, evidence heard in the music, a reason", taught as new
  because ELA grade 8's argument unit comes later; day 149: "claim, evidence heard, why it shows intent". Music 9 to
  12 (days 82, 130, 242, 290, 450, 511): "a claim, evidence from the music, reasoning frame". Grades 6 and 7 write
  responses with no claim card at all.
- **Why it matters.** A shared card that changes its words each band reads to a student as a new tool, and grade 8
  re-teaches from zero a form the student used two years before. The ELA lean on day 137 is right; the starting
  point is not.
- **Fix.** One card, from grade 5 on: "Claim. Evidence from the music (what you hear, with a time or a bar). Reason
  (why that evidence shows the claim)." Music 3 to 5 day 132 and music 9 to 12's bridge line use those words; music 6
  to 8 day 137 opens as a retrieval of the grade 5 card (it is two grades back, so a ten-minute reteach by the card,
  not a new teach), then adds the student's own criteria; day 149 keeps its third step as "Reason: why it shows
  intent". Grades 6 and 7's written listening items (days 17 and 81) name the same card.
- **Tag: scope.**

### 5. Grade 6 steps back from grade 5 on I and V

- **Courses and days.** Music 3 to 5 day 146 (grade 5) sings the I and V chords "in three groups (root, third,
  fifth)", day 148 invents two accompaniments on them, day 163 writes I and V chord symbols over a melody and day 179
  reads them in the concert piece. Music 6 to 8 day 41 (grade 6) has students "find its two chords (I and V) by
  singing the chord roots under the tune", taught as an Understanding day, after day 40 has already retrieved
  mu-g5-document (two-chord harmony).
- **Why it matters.** The technique gets easier from grade 5 to grade 6 (roots only, after full triads), against bar
  item 2; a student who took music 3 to 5 is taught a smaller step than the one already met.
- **Fix.** Music 6 to 8 day 41 goal: "Sing 'Down in the Valley' over its I and V chords (the grade 5 triads, sung in
  three groups) and hear by ear where the chord changes; hear how Piazzolla's 'Libertango' ..." with the note "builds
  on music 3 to 5 days 146 and 163; the roots-only line is the reteach and free path". No day moves.
- **Tag: scope.**

### 6. Two repeats across bands carry no named reason, one of them made by a fix

- **Courses and days.** Vivaldi's "Spring" was added to music K to 2 day 73 by that course's fix pass (kept by the
  lead, DESK-ANSWERS 2026-11-26). Music 6 to 8 then makes it the central listening study of unit 5 (days 67, 71 to
  73) with no line that grade 1 heard it. Music 9 to 12 names every one of its revisits ("a named revisit (music K
  to 2 hears The Entertainer)", days 8, 203, 363, 401); 6 to 8 names none. The same holds for the powwow social song:
  music 3 to 5 day 1 (grade 3) and music 6 to 8 day 51 (grade 6) both hear one, for different jobs (the listening
  routine, then venue and manners), and neither says so.
- **Why it matters.** Rule 2 (repeats) asks for the reason in the scope; and a teacher in grade 6 who sees "Spring"
  should know to start from what the class remembers, not from scratch.
- **Fix.** Music 6 to 8 day 67 note: "A named revisit: music K to 2 day 73 heard its opening beside a spring
  picture; here the whole movement's form and its sonnet." Day 51 note: "A named revisit of the genre: music 3 to 5
  day 1 heard an intertribal social song for listening; here the venue and its manners." The scope's unit 5 and
  unit 4 sections each add that sentence.
- **Tag: scope.**

### 7. The powwow is a leave-out study in grade 6 but not in grade 3, where it is the band's first day

- **Courses and days.** Music 6 to 8 days 51, 53 and 61: "a school may leave the powwow study out", with the assembly
  route that keeps MU:Pr6.1.6b met. Music 3 to 5 day 1 (grade 3, the hook that sets the listening routine) and day 9
  hear and describe a powwow social song with the same ceremonial caution, but name no leave-out or swap.
- **Why it matters.** STANDARD.md 5 lets a school leave out a work for its community's reasons and keeps the ids met
  by a swap. The same tradition is treated as optional in one band and fixed in another; and because grade 3's
  powwow sits on day 1, a school that drops it has no named replacement for the day that teaches the routine.
- **Fix.** Music 3 to 5 day 1 note adds: "A school may swap the powwow listen for a living Native American maker's
  non-ceremonial concert or social work (the unit plan names one, not Tate, Ballard or Davids, who are placed
  elsewhere); the routine and MU:Re7.2.3a are taught on it the same way." Day 9's four-box example names the swap's
  setting as the other option. The scope's unit 1 paragraph says so in one line.
- **Tag: scope.**

### 8. K to 2 and 3 to 5 still carry the `end` workaround the gate no longer needs

- **Courses and days.** Music K to 2 days 36, 48, 96, 112, 160, 176 and music 3 to 5 days 28, 46, 92, 110, 156, 174
  are supported practice days marked `end` only so scripts/sequence.py would pass (both scopes' For the lead 1).
  Since the computer science scope calls of 2026-11-26, sequence.py accepts a course-level check on the day right
  after a unit's last day as its end-of-unit assessment, and the CS courses cleared their marks. Music 6 to 8 used a
  third workaround (showing days 34, 98, 162 as Check, end), which is honest there because the performance item is
  heard that day.
- **Why it matters.** A lead call applied in one subject and not another; and an `end` mark on a practice day tells a
  unit writer that the day is the assessment, when the check day is.
- **Fix.** In music K to 2 and 3 to 5, clear `assess` on those twelve days, move the kept-work codes they carry onto
  the next day's check row (scored from the kept page, as the check goal already says), and drop For the lead 1 from
  both scopes. Run sequence.py check after. Music 6 to 8's showing marks stay, with finding 2's fix.
- **Tag: scope.**

### 9. Safety rules drift between bands: the changing voice and hearing protection

- **Courses and days.** The changing-voice rule ("a changing voice chooses its octave or speaks the rhythm") is on 76
  music 6 to 8 days and on no music 9 to 12 day, though Level 1 sight-sings "in each clef" (days 6, 7, 11) and many
  grade 9 students are mid-change. Hearing protection or a quiet seat is offered on 25 K to 2 days and in the 3 to 5
  daily rules, and on no 6 to 8 or 9 to 12 day, though 6 to 8 uses buckets and sticks daily and 9 to 12 uses found
  percussion and headphones.
- **Why it matters.** A safety rule that stops at a band line is a rule a teacher at the next band does not see
  (bar item 9, "safe use of space"; APPROACH safety line on loud sound).
- **Fix.** Music 9 to 12: every day that sings adds "a changing voice chooses its octave or part and is never named"
  to its voice line. Music 6 to 8 and 9 to 12: the safety line on days with drums, buckets or loud playback adds
  "hearing protection or a quiet seat allowed", in K to 2's words.
- **Tag: scope.**

### 10. "If a student tells you something" is on the personal-tie days in K to 2 and 9 to 12 only

- **Courses and days.** Music K to 2 days 26, 29, 89, 90, 154, 155 and music 9 to 12 days 25, 82, 179, 339, 403, 485,
  563 carry "health's steps if a student tells you something" on the days that ask about tastes, experiences or a
  hard history. Music 3 to 5 (Cn10 and Re7.1 days 6, 14, 70, 78, 134, 142; Makeba's exile day 129) and music 6 to 8
  (days 26, 27, 90, 154) carry none, though they ask the same kind of question.
- **Why it matters.** APPROACH puts health's steps on every section's teacher page; two bands flag where they are
  most needed and two do not, so the middle bands' unit writers are the likeliest to leave the line off.
- **Fix.** Add the K to 2 sentence to those 3 to 5 and 6 to 8 days' notes.
- **Tag: scope.**

### 11. The critique card is worded seven ways across the group

- **Courses and days.** K to 2 frame and 3 to 5: "describe what you hear, ask about a choice, suggest one change";
  6 to 8 uses six forms on its critique days ("ask about one choice", "one reading", "one interpretive choice", days
  13, 30, 46, 58, 77, 94); 9 to 12 "describe, ask, suggest" (days 39, 65, 101 and on). The critique-protocol model is
  one card carried by name from kindergarten to Level 4.
- **Why it matters.** Small, but a shared card should read the same so a student recognizes it; the variants also
  drop "tied to a look-for" in places, which is the part that stops praise-only feedback (lens, Unit errors).
- **Fix.** One wording on every critique day of the four courses: "Describe what you hear. Ask about one choice.
  Suggest one change tied to a look-for." Each day may add what the choice is about after a colon (a reading, an
  interpretive choice), not by rewording the card.
- **Tag: scope.**

### 12. Grade 6's composing unit gives less making time than grade 5's for a harder piece

- **Courses and days.** Music 3 to 5 unit 11 (grade 5, 16 days) has six making days around its critique (164, 167
  to 170, 173). Music 6 to 8 unit 3 (grade 6, 12 days) asks for a notated AB or ABA piece with chords and has two
  making days before the critique (43, 45), with Fluency day 44 between them. Grades 7 and 8 (units 7 and 11) have
  the same shape. The unit 4 revision days (52, 54, 59) partly make this up, which is why this is not a structure
  finding.
- **Why it matters.** The demand rises from grade 5 to grade 6 while the making time falls by half, a jump the scopes
  do not ramp (check 5); a writer will over-fill day 45.
- **Fix.** Music 6 to 8 day 44 (and its twins 108 and 172) becomes an Application day, "Draft the piece's A section
  over I and V, with the chord-root round and dictation as the five-minute opener", so each composing unit has three
  making days before the critique. Day 44 is also a named fold-in day in the shorter path; swap that fold-in for
  spare day 56 and say so in the table.
- **Tag: scope.**

## What holds

- Every owned row of the 100 music rows is taught and assessed in its own course (script check), apart from finding
  2; Level 4's `~` ids are applied again, not left begun.
- The seams match at both ends: each band's "handed on" table names the same eight rows the next band's "picked up"
  table does, and each scope's retrieval table cites the right days of the course before (3 to 5 checked against K to
  2's days 129 to 192; 6 to 8 against 3 to 5's days 144 to 192). 9 to 12's readiness checks for students new to music
  are the frame's settled choice.
- Calendar: every check is on its CALENDAR.md target week (K to 2 weeks 19 or 17 and 25, 3 to 5 weeks 15 and 24, 6
  to 8 weeks 19 and 32, 9 to 12 weeks 16 and 32); `frame.py calendar` reports no break. The school_day counting is
  stated once in each scope, by band in K to 8 and by level in 9 to 12, as the lead call allows.
- Shorter paths are present and built the same way in all four (named fold-in days, a once-a-week path in K to 8,
  an 80-day semester in 9 to 12).
- Works range widely across the group, with living makers and named Native American makers in every band; 9 to 12
  names each revisit of a K to 8 maker (Joplin, Mozart, Beethoven, Dvořák), and no other work repeats.
- Sacred and ceremonial material is listening only in every band, with the same "told as a claim" handling of
  Dvořák in 3 to 5 day 68 and 9 to 12 day 402.
- The no-solo rule, recording consent and the invented option on Cn10 days hold in all four.

## Sources

- https://en.wikipedia.org/wiki/Margaret_Bonds, opened 2026-11-26: Bonds studied with Florence Price, was born in
  Chicago; Montgomery Variations dated 1964 (some sources 1965) on "I Want Jesus to Walk with Me" (9 to 12 days 81,
  82 hold).
- https://en.wikipedia.org/wiki/Symphony_No._1_(Price), opened 2026-11-26: "Juba Dance" is the third movement; the
  page describes juba as an American dance with body percussion (K to 2 day 179 holds). Price's Little Rock birthplace
  is from memory.
- From memory, not opened: Bernstein's December 1989 Berlin Ninth with "Freiheit" (3 to 5 day 137); Joanne
  Shenandoah's dates and Oneida Nation (K to 2 day 151); the dates of the Haydn, Grieg, Beethoven Fifth and Mozart
  K. 331 works on their days. No page refused a read; nothing is marked browser check.
- The syllable and solfege pick in finding 3 rests on memory of common open early-grade practice, not on a source
  read here.

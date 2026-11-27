# Scope group fixes: music, K to 12 (2026-11-26)

Fix pass for docs/reviews/scope-group-music-2026-11-26.md (11 scope findings, 1 frame finding), done to
build/scope-writes/GROUP-FIX.md with the ARTS-FIX.md lead calls kept. Courses touched: music-grades-k-to-2,
music-grades-3-to-5, music-grades-6-to-8, music-grades-9-to-12. No unit moved, no day count or owned row changed.
days.csv edited with the csv module, quoting and line endings kept (K to 2 and 6 to 8 CRLF, 3 to 5 and 9 to 12 LF).

## Applied

1. **Key signatures (scope).** Music 9 to 12 day 6 now teaches "major key signatures to three sharps and flats
   (finding do from the signature), with the step card" before the sight-singing; day 175 adds "relative minor and
   all key signatures on the circle of keys". Music 6 to 8 day 131's first step is "key, the key signature of G or F
   from day 2's sharp and flat, and meter", taught on the day's step card; the unit 9 paragraph and the 9 to 12
   bridge paragraph say so.
2. **MU:Pr4.1.6a, 7a, 8a scored (scope).** Added to the codes of check days 37, 101 and 165. Their notes already said
   the kept program page or note from days 35, 99 and 163 is scored after the session, once; the scope's check table
   already named them.
3. **Syllable and solfege systems (frame, the read's pick, as plain wording).** Each of the four frames' Models
   carried row for rhythm-syllables now ends with the same sentence: rhythm by "ta", "ti-ti", "ta-a" and the rest,
   with "ti-ka-ti-ka" for sixteenths, beside beat numbers from grade 3; pitch by movable do with la-based minor,
   growing from so, mi and la (K to 2) to the pentatonic (grade 3) and the full major scale (grade 4), kept beside
   letter names from grade 4 on; a school may use its own systems instead, as long as it keeps one through the band.
   Day wording followed: K to 2 day 133 names the syllables (the rest felt as a silent beat) instead of "a spoken
   counting system"; 3 to 5 days 117 and 178 read by letter names and solfege; 6 to 8 day 131 reads rhythm "on the ta
   and ti-ti syllables" and sings the line in solfege; 9 to 12 day 4 names the syllables, and day 6's note makes its
   solfege a named revisit for a student from music 3 to 5 and 6 to 8, new for a student without it.
4. **One claim-and-evidence card (scope).** Wording: "Claim. Evidence from the music (what you hear, with a time or a
   bar). Reason (why that evidence shows the claim)." Used on 3 to 5 day 132 (two pieces of evidence at that grade),
   6 to 8 days 17 and 81 (written listening items), day 137 (now opens with a ten-minute reteach of the grade 5 card,
   then the student's own criteria; its ELA note and the scope's lean paragraph reworded), day 149 (third step kept
   as "Reason: why it shows intent"), and the 9 to 12 bridge line on all 17 days that carry it.
5. **Grade 6 on I and V (scope).** 6 to 8 day 41 sings "Down in the Valley" over its I and V chords (the grade 5
   triads, in three groups) and hears where the chord changes; its note says it builds on music 3 to 5 days 146 and
   163 and the roots-only line is the reteach and free path. Unit 3 paragraph names it.
6. **Named revisits (scope).** 6 to 8 day 67 note and the unit 5 paragraph: Vivaldi's "Spring" is a named revisit of
   music K to 2 day 73. Day 51 note and the unit 4 paragraph: the powwow social song is a named revisit of the genre
   from music 3 to 5 day 1.
7. **Powwow swap in grade 3 (scope).** 3 to 5 day 1 note names the swap (a living Native American maker's
   non-ceremonial concert or social work, not Tate, Ballard or Davids; the routine and MU:Re7.2.3a taught the same
   way); day 9's four-box card names the swapped work's setting as the other option; the unit 1 paragraph says so.
8. **`end` workaround marks (scope).** Removed: sequence.py check passes with 0 failures after the change. `assess`
   cleared on K to 2 days 36, 48, 96, 112, 160, 176 and 3 to 5 days 28, 46, 92, 110, 156, 174. The kept-work codes
   were already on each following check row, so no codes moved; the notes now read "Kept work for the end-of-unit
   assessment: ..." and still say the item is scored once from kept work with the check. Both scopes' "For the lead
   1" dropped and the rest renumbered; K to 2's "How the band runs" paragraph and 3 to 5's unit paragraphs (units 2,
   3, 6, 7, 10, 11) no longer mention `end`. Music 6 to 8's showing marks (days 34, 98, 162) stay, as the read says.
9. **Safety drift (scope).** Music 9 to 12: the changing-voice rule ("a changing voice chooses its octave or part
   and is never named") added to the voice line on all 133 days that carry it, to day 547's reviewer line, and a
   full voice line added to the 8 singing drill and portfolio days that had none (16, 45, 60, 111, 199, 330, 336,
   359): 142 days in all. "Hearing protection or a quiet seat allowed" added to the 76 music 6 to 8 bucket and drum
   safety lines and the 12 music 9 to 12 found-percussion days.
10. **"If a student tells you something" (scope).** K to 2's sentence added to 3 to 5 days 6, 14, 70, 78, 129, 134,
    142 and 6 to 8 days 26, 27, 90, 154.
11. **One critique card (scope).** Wording: "Describe what you hear. Ask about one choice. Suggest one change tied to a
    look-for.", with what the choice is about after a colon where a day had it ("an interpretive choice" on 6 to 8
    day 30, "a reading" on 94 and 158) and a dress rehearsal's look-for area after the card (58, 122, 186). Applied
    on every day that spelled the card out: K to 2 days 14, 34, 46, 76, 94, 109, 140, 158, 173, 187; 3 to 5 days 8,
    10, 74, 138 and the model notes of 8, 72, 136, plus the scope's band paragraph; 6 to 8 days 13, 30, 46, 58, 77,
    94, 110, 122, 141, 158, 174, 186; 9 to 12 days 10, 39, 65, 101, 132, 144, 193, 221, 263, 304, 353, 381, 420, 464,
    496, 507, 532, 546, 552, 575, 589, 618. Days that only name "the critique routine" were left as they are.
12. **Grade 6 to 8 composing time (scope).** Days 44, 108 and 172 changed from Fluency to Application drafting days
    (the A section; the theme and first variation; the introduction and two sections), with their drills as the
    five-minute opener; codes and skills unchanged. In the shorter path, day 56 replaced day 44 as the fourth fold-in
    day (moved up from the spares, with a line saying so), and the once-a-week merges for units 3, 7, 11 now read
    "41+42; 43+44+45" so the drafting day sits with the making days (same six sessions). Unit 3, 7 and 11 paragraphs
    name the new days.

## Rejected

None.

## For the structure pass

None from this read (it had no structure finding). One small leftover: music 9 to 12 frame.md's Cross-subject row
(units 4, 9, 14 and 17) still words the bridge as "the claim, evidence from the music, reasoning frame"; I left it,
since frame.md was open here only for finding 3. The lead may align it with the card in finding 4.

## For Cory

None (the read had no Cory finding).

## Ledger

29 rows logged with `scripts/plan.py defect --status=fixed --made-at=scope ... scope expert`, one per finding per
course touched (four frame.md rows for finding 3). Two summaries carry slightly low counts (finding 9's 9 to 12 row
says 141 days, the right count is 142; finding 11's 3 to 5 row says 7 days, the right count is 6 days plus the scope
paragraph).

## Checks

- `scripts/sequence.py check`: 0 failures on all four courses (9 to 12 prints its usual seven "standard None is on
  no day" notes for Level 4).
- `scripts/frame.py check`: 0 failures on all four courses.

# Scope group fix pass: media arts, K to 12 (2026-11-26)

Fixes for docs/reviews/scope-group-media-arts-2026-11-26.md, per build/scope-writes/GROUP-FIX.md, on
media-arts-grades-k-to-2, media-arts-grades-3-to-5, media-arts-grades-6-to-8 and media-arts-grades-9-to-12. The
ARTS-FIX.md lead calls still hold and were not re-decided. No unit moved, no day count or owned row changed. days.csv
edits used the csv module, CRLF line endings and minimal quoting kept (a round trip was checked byte for byte first).

## Applied

- **Finding 2 (scope).** 3 to 5 scope, "Codes not sampled on a course-level check": the stale reason (the year-end
  check "sits before the core year-end weeks 28 to 32") is replaced by K to 2's wording: the frame keeps the year-end
  check before the screening unit, and the older reason no longer holds under CALENDAR.md rule 1, with a pointer to
  finding 1 of the group read. The frame's "CALENDAR.md stagger tool c" sentence goes with finding 1, so it is left
  for the structure pass.
- **Finding 3 (scope).** 3 to 5 scope, "A shorter period (30 minutes)": the end-of-unit talk-and-written day stays a
  check day; the six talk groups are heard at the teacher's table while the class writes the item and the self-check
  (set-up 4, tables 15 while the groups take 18, clean-up 3: 25 minutes, 5 slack); if a class needs longer, the
  self-check moves to the end of the day before (the K to 2 rule). No talk item moves onto a making day. The APPROACH
  "Kinds of day" exception is struck from the scope's For the lead item 6. The 3 to 5 fixes report
  (docs/reviews/sequence-media-arts-grades-3-to-5-fixes-2026-11-26.md, structure item 2) is not mine to edit; the lead
  should treat that item as dropped.
- **Finding 4 (scope).** One word set:
  - Shot sizes: 3 to 5 days 3 and 5 say "wide, medium, close", and day 3's note names the far, middle and close shots of
    grades K to 2; the 3 to 5 frame's three matching phrases (techniques line, unit 1 row, fluency call) changed to
    match. K to 2 keeps "far, middle, close". The cut-in close-up of grade 5 (days 40, 167, 169) is a different shot and
    stays. 6 to 8 day 2: "wide (long), medium, close".
  - Plan card: 6 to 8 days 56, 120, 184 notes say "the showing-plan model"; day 50's note adds "grade 5's
    screening-plan card grows into the showing plan". 9 to 12 days 11, 74, 111, 118, 161, 164, 271, 431 say "showing
    plan", and also day 10 (the bridge's card itself, which the read did not list but which would otherwise keep the
    old name), the scope's bridge arc (unit 1) and the frame's unit text (five "screening-plan card" phrases and the
    unit 6 readiness line). The `screening-plan` model id in both frames' model tables is an internal id and stays.
  - 6 to 8 day 2: "the media-literacy checklist".
  - 9 to 12 day 2: "Look-describe-interpret taught on one still (the reading steps of grades 6 to 8, given one name
    here)". Day 3 never named the routine, so only day 2 changed.
- **Finding 5 (scope).** 3 to 5 day 80: returns from K to 2 day 153; new are replacement parts and the even move. 6 to 8
  day 2: returns from 3 to 5 days 3 and 4; new is what each size steers in a sequence (also in the goal). 6 to 8 day
  36: returns from 3 to 5 day 4; new is the point-of-view shot. 6 to 8 day 18: the day now teaches frame-by-frame
  timing (holds, frames per second, drawings spaced for ease in and ease out) on the stop-motion sequence, the ordinary
  use kept for MA:Pr5.1.6c; the 12-drawing flip book is the five-minute opener warm-up; the note names the return
  from 3 to 5 days 16, 80 and 146. The 6 to 8 unit 2 arc says the same. No day moved; `retrieves` unchanged.
- **Finding 6 (scope).** 9 to 12 day 44: the opener's retrieval now recalls grade 8's thinking in many directions (6 to
  8 day 144) and grade 6's methods card (6 to 8 day 16), with the reteach of the "what if" list for a student new to
  media arts; the new method is the forced pairing. Day 45 teaches a second new method, the random-word link. The
  two-method look-for on days 44 to 46 is unchanged. The frame's MA:Cr1.1.I wording named the old pair, so its
  parenthetical now reads "a forced pairing of two unrelated things and a random-word link, after grade 8's methods
  and the "what if" list are retrieved".
- **Finding 7 (scope).** 9 to 12 day 321 already named Hopinka's return from Jáaji Approx.; the note now reads "with a
  different film and a harder question", as the read asks.
- **Finding 8 (scope).** 9 to 12 days 2, 6, 7, 8, 30, 31, 32, 33, 34: "no filming of anyone without their yes, and the
  family's for a student under 18 (a student 18 or over decides alone; the school's own rules apply)".
- **Finding 9 (scope).** K to 2 days 86, 109, 156, 173: same-year retrievals are five-minute warm-ups in the opener;
  the cross-year ones stay ten (rule 2); the scope paragraph on same-year retrievals says the same. 6 to 8 fold-in
  days 9, 24, 41, 53, 67, 72, 88, 117, 136, 152, 165, 181: the drill moves into the next opener as a 5-minute warm-up
  and saves 35 minutes; the scope's Shorter path says 35 minutes each, 140 a year.

## Rejected

None. Every finding read true against the files.

## For the structure pass (not applied)

- **Finding 1, structure: the K to 5 year-end check week.** K to 2 (weeks 27, days 53/54, 117/118, 181/182) and 3 to 5
  (weeks 26/25/25, days 51/52, 113/114, 177/178) hold the year-end check before the screening unit; 6 to 8 and 9 to 12
  hold it in week 32, after. The old reason (staying off the core weeks) no longer holds under CALENDAR.md rule 1, and
  42 of 54 ids in K to 2 and 31 in 3 to 5 are never sampled at course level. Options: (a) move each year-end check and
  its respond day to week 32, after the screening unit, sampling the second unit's ideas row and the third unit's judge
  row and carrying the screening unit's record (as 6 to 8 does), with the frames' check tables, once-a-week bullets,
  the units-table phrases "after the year-end check" and CALENDAR.md's target weeks changed (K to 2 "21, 27" to
  "21, 32"; 3 to 5 "17, 26 / 17, 25 / 18, 25" to "17, 32 / 17, 32 / 18, 32"), then the course fixers re-lay days.csv;
  (b) keep the early weeks. The read's pick: (a), as one call for the K to 5 pair (it merges K to 2 fix report structure
  item 1 and 3 to 5 fix report structure item 5). The 3 to 5 frame's "CALENDAR.md stagger tool c" sentence (finding 2's
  frame half) goes with this call.
- **Dropped:** 3 to 5 fix report structure item 2 (an APPROACH "Kinds of day" exception for the 30-minute period),
  made unnecessary by finding 3.

## For Cory

None.

## Defect ledger

Ten rows logged with `scripts/plan.py defect --status=fixed --made-at=scope`: K to 2 days.csv and scope-and-sequence.md;
3 to 5 scope-and-sequence.md, days.csv and frame.md; 6 to 8 days.csv and scope-and-sequence.md; 9 to 12 days.csv,
scope-and-sequence.md and frame.md.

## Checks

| Course | sequence.py check | frame.py check |
|---|---|---|
| media-arts-grades-k-to-2 | 0 failures | 0 failures |
| media-arts-grades-3-to-5 | 0 failures | 0 failures |
| media-arts-grades-6-to-8 | 0 failures | 0 failures |
| media-arts-grades-9-to-12 | 0 failures (its expected Level 4 notes, units 16 to 19 with no new id) | 0 failures |

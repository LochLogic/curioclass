# Scope group read: theater, K to 12 (2026-11-26)

Brief: build/scope-writes/GROUP-READ.md. Courses: theater-grades-k-to-2, theater-grades-3-to-5,
theater-grades-6-to-8, theater-grades-9-to-12. This read looks across the four scopes; it does not repeat the
single-course reads or their fix passes.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/ARTS-BRIEF.md.
- docs/agents/lenses/arts.md; docs/ADOPTION-BAR-SUBJECTS.md section 2; docs/courses/arts/STANDARD.md 3.1 to 3.4;
  docs/courses/arts/APPROACH.md ("Family note", "Sensitive ground").
- data/progressions/arts.csv, all 98 theater rows (by script). There is no arts-edges.md file; the `assumes` and
  `hands_on` columns were read instead.
- For each course: scope-and-sequence.md in full; the frame's Models table, Units table hazards and sensitivity
  lines (by search); data/plans/<course>/days.csv by Python script (code coverage, kinds, assess slots, and keyword
  passes over goal and note for models, works, safety lines, sensitivity lines and written-day load).
- The four sequence reads and their fix reports (searched for what was settled); the arts frame fix review
  (frame-music-theater-media-arts-fixes-2026-11-26.md, revisit swaps).
- docs/courses/CALENDAR.md rules 1, 3 and 4 and the theater rows; DESK-ANSWERS.md 2026-11-26 entries "arts scope
  lead calls" and "after-core frame calls".

Script checks that pass: every owned id of each grade or level is carried by a day and sits on an assessment day
(65, 72, 72, 72); each 6 to 8 retrieval names the right grades 3 to 5 unit for its grade 5 row; each 3 to 5
retrieval names the right K to 2 unit for its grade 2 row.

## Findings

1. **Seam: the 9 to 12 bridge assumes stage areas and blocking from grade 8, and 6 to 8 never teaches them.**
   Theater 9 to 12 day 1 sets the readiness check on "the warm-up routine, stage areas and blocking, script markup
   and the critique protocol" as grade 8 techniques, and says a student who took 6 to 8 "meets the same items as
   retrieval"; days 2 and 3 reteach stage areas, blocking, cheating out and levels (frame Units row 1: "Words: stage
   left, downstage, blocking"). Theater 6 to 8 has no day that names stage areas, blocking, cheating out or levels
   (0 of 192 days); its staging days (22 to 24, 87, 164) work on staging problems and venues without them. Why it
   matters: a Curio Class grade 8 student is marked "not yet" on a technique nobody taught, and the readiness record
   then sends them to the wrong bridge days. Fix (pick): 6 to 8 teaches stage areas and blocking in steps on day 23
   (the walking-pace run of the key events, a taped stage-areas floor card) and uses them again on day 164 (the venue
   plan), with "stage left, downstage, blocking" added to those days' Words. Other way: 9 to 12 day 1's note moves
   stage areas and blocking out of the readiness items and calls days 2 and 3 first teaching. **scope**

2. **Seam: 6 to 8 calls models "first used" that grades 3 to 5 already taught.** 6 to 8 notes say "model first
   used" for the audience journal (day 1), character map (3), what-if list (22), prop sketch (36), cue sheet (37),
   criteria card (39) and two-ties card (50). The 6 to 8 frame's own Models table gives each an earlier origin, and
   3 to 5 teaches them: character map day 21, audience-journal card days 24 and 30, what-if list day 2, prop sketch
   day 36, two-ties card day 41, criteria card day 59, cue sheet day 167. Only script markup (6 to 8 day 20) and
   reason-because (day 39) are new in grade 6. Why it matters: a teacher reads "first used" and teaches a known card
   from scratch, and the band misses the retrieval the frame planned. Fix: in those seven notes write "returns from
   Theater, grades 3 to 5 unit n; here ...", naming what grows (the frame's Models table already says what). **scope**

3. **Load: the written day jumps from grade 5 to grade 6 with no ramp and loses the spoken option.** 3 to 5 written
   days hold at most two written items in 15 minutes, and "a student may answer aloud at the table, marked the
   same" (days 161, 190 and every written day). 6 to 8 day 17, in week 9 of grade 6, sets four ids in 25 written
   minutes (TH:Cr3.1.6b, TH:Re7.1.6a, TH:Re8.1.6a, TH:Re8.1.6c); days 47, 81, 111, 145 and 175 set three; no 6 to 8
   written day carries the spoken option. W.6.1 (claim and evidence) is still being taught in ELA grade 6 units 1
   and 2. Why it matters: the first middle school check doubles the written load the band just capped, and a
   student who wrote little in grade 5 loses the route the earlier course gave. Fix: every 6 to 8 written day's note
   adds "a student may answer aloud at the table, marked the same"; day 17 moves TH:Cr3.1.6b (body and voice traits
   that work) to day 16's showing as a live look-for, where the mid-year check (day 33) already marks it live, so
   day 17 holds three items. **scope**

4. **Calendar: the once-a-week path treats the mid-year check three ways, and 6 to 8 keeps the problem 3 to 5
   solved.** On the once-a-week path, 3 to 5 drops each year's mid-year check and gives the two sessions to the
   design unit (units 3, 7 and 11 get 9, 9 and 8 sessions, no session over three days). K to 2 keeps both checks
   (weeks 17 and 26); its design units already keep a making session of their own. 6 to 8 keeps both (weeks 17 and
   31) and its design units (3, 7, 11) still put a making day, a tech rehearsal and a critique into one or two
   sessions (its For the lead item 1, open). Why it matters: the same failure the 3 to 5 fix pass removed is left
   in the band that follows it. Fix (pick): the 6 to 8 frame's once-a-week path drops the mid-year check, as 3 to 5
   does (every id is still assessed in its own unit), and gives unit 3, 7 and 11 the two freed sessions (6 to 8),
   one of them a making session alone. The other route is the dance 6 to 8 timed written block (DESK-ANSWERS,
   2026-11-26, already named for theater 6 to 8 in the structure pass). **frame**

5. **Drift: the 3 to 5 floor line drops the no-lifts and no-contact rule its own frame sets.** The 3 to 5 frame's
   hazards say "no lifts, no falls rehearsed, no contact stage fights"; the 3 to 5 days' floor line (days 1, 17, 35,
   55, 65, 81, 99, 117, 129, 145, 165, 183, and the band page's equipment bullet) says only "freezes held still, no
   falls". K to 2 days carry "no lifts or falls" (27 days) and "no contact fights" (111 to 114); 6 to 8 carries "no
   lifts, no falls, no contact"; 9 to 12 "no lifts or falls; partner contact by agreement only" with no contact
   stage fights. Why it matters: grades 3 to 5 are the years of the hot seat, the wordless pair scene and Chaplin's
   walk, where a pratfall or a shove is most likely, and the day line is what a teacher reads. Fix: the 3 to 5 floor
   line and band page add "no lifts, no contact stage fights". The ramp across the group (no contact to grade 8,
   partner contact by agreement in 9 to 12, never a stage fight) holds and needs no change. **scope**

6. **Sensitivity: which works get a content note to families is not settled, and the courses split.** 9 to 12 gives
   a "content note to students and families" for Sweat (day 224) and Sovereignty (days 417 to 432), but not for
   Twilight: Los Angeles, 1992 (day 68: the unrest after a police beating). 6 to 8 studies apartheid through Woza
   Albert! (days 179, 182), the government stopping Kamiriithu (118) and the housing covenant case (73) with "named
   plainly" and no family note; 3 to 5 names the grape strike (165) the same way. APPROACH "Family note" says only
   that each unit has one. Why it matters: two works of the same kind (state violence, described, never performed)
   get a family note in one course and none in the next, so families are told in grade 11 what they were not told
   in grade 8. Fix (pick): the lead states the threshold once in docs/courses/arts/APPROACH.md "Sensitive ground":
   a content note to families (to the student at 18 or over) when a studied work's subject includes violence
   against a person, a killing, sexual violence or drug use, even when only described; other hard history is named
   plainly with no note. Then 9 to 12 day 68 and 6 to 8 day 179 get the note, and days 73, 118 and 165 stay as
   they are. If the lead reads this as an audience call, it goes to Cory with this pick. **frame**

7. **Repeats: three revisits across bands are not named, where the others are.** 6 to 8 names its revisits of
   commedia (day 19), Stanislavski (132), Spolin (134), Shakespeare (163) and kabuki dance from dance 3 to 5 (99);
   9 to 12 names Shakespeare (327) and Arena Stage (417). Not named: 9 to 12 day 167 (noh and Hagoromo) after 3 to 5
   day 17 met kyogen "on a day of noh"; 9 to 12 day 328 (the kabuki borrowing in Les Atrides) after 6 to 8 unit 7
   (day 99 on); 6 to 8 day 177 (Boal's forum theater) after 3 to 5 unit 11 (El Teatro Campesino, day 165, and
   Laedza Batanani, day 169, a popular-theater project in the same participatory line), a second "theater about a
   community's problem" unit with no reason given. Why it matters: the bar's repeat rule asks for the reason, and a
   teacher who sees the case again cannot tell revisit from slip. Fix: one "named revisit" line each, with the new
   job (noh's own form after its comic sibling; kabuki as a borrowed tradition, not a studied one; the audience
   stepping in, which the 3 to 5 sign plays did not ask). **scope**

8. **Repeats: shadow theater four times in K to 5, twice in year 4, each with the same lamp-and-screen task.**
   Chinese shadow puppetry (K to 2 day 42), Karagöz (day 165), wayang kulit (3 to 5 day 71) and tholu bommalata
   (day 101), with the flashlight-and-screen cue in K to 2 days 42 to 43, 166 and 3 to 5 days 99 to 101. The frame
   fix pass rightly swapped plain revisits for new traditions; what is missing is the reason for two in one year and
   for the same task form. Why it matters: Asia's range in K to 5 leans on one form, and grade 4 meets it in units 5
   and 7. Fix: 3 to 5 day 101's note names it as a revisit of the year's wayang with a new job (the lamp as a tech
   element serving a central idea, not the dalang's many jobs), and K to 2 day 165 names Karagöz against year K's
   shadow day; the unit 7 plan may swap tholu bommalata for a non-shadow light or sound tradition at no day cost.
   **scope**

9. **Drift: K to 2 counts school_day another way than 3 to 5 and 6 to 8.** K to 2 fills school_day as the second
   and fourth school days of each week (2 to 479); 3 to 5 and 6 to 8 use ceil(2.5 n) (3 to 480), the even spread
   frame.py writes, so calendar.csv already disagrees with K to 2 only (K to 2 For the lead item 2; 3 to 5 item 2,
   open). Why it matters: one rule across the group keeps calendar.csv and days.csv the same without a lead
   regenerate, and the K to 2 formula is the only one a reader must learn separately. Fix: K to 2 refills school_day
   as ceil(2.5 n) across the band; course day k of a year still sits in week ceil(k / 2), so no unit or check moves,
   and the .md's school_day bullet takes the 3 to 5 wording. **scope**

10. **Drift: shared cards worded differently from band to band.** The group-agreements card reads "take turns, add
    on, freeze on the signal, join when ready" in K to 2 (day 8) and "take turns, build on, freeze on the signal,
    keep the space safe" in the 3 to 5 frame; the warm-up routine is "body, voice and thinking" (3 to 5), "body,
    breath, voice, focus" (6 to 8 day 2) and "body, breath and voice" (9 to 12 day 2); 3 to 5 day 2 shows the freeze
    "in named steps" as if new, after K to 2 days 2 and 3 taught freeze and melt. Why it matters: a card that grows
    should keep its old lines so a student recognizes it. Fix: each card grows by adding lines: agreements "take
    turns, add on, freeze on the signal, join when ready" from K, plus "keep the space safe" from grade 3; warm-up
    "body, voice, thinking" to grade 5, then "body, breath, voice, focus" from grade 6 through 9 to 12; 3 to 5 day 2
    names the freeze as K to 2's freeze and melt with the breathe step added. **scope**

Count: 8 scope, 2 frame, 0 structure, 0 Cory.

## What holds

- No gaps: every theater id K to 8 and Levels 1 to 3 is taught and assessed in its own year or level; Level 4's `~`
  rows reassess Level 3 ids as STANDARD.md 3.2 sets.
- Retrieval seams across bands are right by grade and unit (3 to 5 on K to 2 units 9 to 12; 6 to 8 on 3 to 5 units
  9 to 12; 9 to 12 day 1 readiness on grade 8, the one place two grades back can occur for a new student).
- The critique protocol is one wording, describe, ask, suggest, on every critique day of all four courses, with a
  clear ramp: teacher-led in K to 2 and 3 to 5 units 1 to 4, student-run from 3 to 5 unit 5, trios in 9 to 12.
- Technique ramps: given circumstances (grade 4), objectives and tactics (grade 8, then the bridge), the character
  map growing from moves, speaks and thinks to goal, motive and tactics; written response from talk items (K to 2)
  to response frames (3 to 5) to claim and criterion (6 to 8) to sittings (9 to 12).
- Named revisits where they are given (commedia, Stanislavski, Spolin, Shakespeare, Arena Stage, kamishibai,
  Marceau) each state the new job.
- Course-level checks sit on CALENDAR.md's weeks in all four, and each names its unsampled ids with the reason.
- Sensitivity guards are the same kind everywhere: no accents, no sacred masks or forms performed, invented or
  public options marked the same, the agent reads the community's own pages first; 9 to 12 carries the 18 or over
  rule.

## Sources

Named facts checked against a page this run (2026-11-26):
- UNESCO, Cultural Space of Sosso-Bala, https://ich.unesco.org/en/RL/cultural-space-of-sosso-bala-00009 (opened):
  proclaimed 2001, inscribed 2008, kept in Guinea; matches 3 to 5 day 57.
- The Unicorn Theatre's 2015 Caucasian Chalk Circle (6 to 8 day 151): confirmed by search results, pages not opened:
  https://www.londontheatre.co.uk/theatre-news/news/caucasian-chalk-circle-at-the-unicorn-theatre,
  https://www.whatsonstage.com/news/the-caucasian-chalk-circle-unicorn-theatre_36996 (January to March 2015).
- Complicité with the National Theatre, 1997 (6 to 8 day 151): confirmed by search results, page not opened:
  https://www.complicite.org/work/the-caucasian-chalk-circle.
- Laedza Batanani, Botswana, from 1974 (3 to 5 unit 11): confirmed by search results, pages not opened:
  https://repository.uneca.org/handle/10855/30130,
  https://www.cambridge.org/core/journals/african-studies-review/article/theater-as-praxis-discursive-strategies-in-african-popular-theater/23E36B83EA66AB96CBCC7F4E84F156E3.
- From memory, not opened, and consistent with the scopes: Scala's printed scenarios (1611), Deaf West Theatre
  (1991; Big River, 2003), El Teatro Campesino (Delano, 1965), Spiderwoman Theater (1976), Kamiriithu (Limuru, 1977),
  Hansberry v. Lee (1940), Spreading the News at the Abbey (1904), Sovereignty at Arena Stage (2018), Appia (1862 to
  1928), Marcks's Bremen statue (1953). The single-course scopes leave each page to its unit plan with a rights line;
  this read opened none of the company pages ("browser check" where a unit plan meets a block).

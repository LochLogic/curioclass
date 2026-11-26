# Frame read: Media Arts, grades K to 12 (four frames, combined), 2026-11-25

Expert cold read under docs/pipeline/briefs/frame-read.md, after-core changes: subject arts, ma-* rows of
data/progressions/arts.csv, STANDARD.md and APPROACH.md in docs/courses/arts/, lens docs/agents/lenses/arts.md. The
four frames are read as one course line, with the seams between bands and the other arts frames of the same band
checked for repeated picks. Check-week clashes are listed in their own section and not counted (the lead's after-core
calendar pass).

## What I read

- AGENTS.md, docs/pipeline/briefs/frame-read.md, docs/agents/EXPERT.md, docs/agents/lenses/arts.md.
- docs/courses/arts/STANDARD.md and APPROACH.md; docs/ADOPTION-BAR-SUBJECTS.md section 2 (Arts).
- docs/courses/media-arts-grades-k-to-2, -3-to-5, -6-to-8, -9-to-12, frame.md, each in full.
- data/progressions/arts.csv (every ma-* row, K to 12), data/plans/frames.csv (the four media arts rows).
- data/standards/ncas-performance-standards-words.txt, the MA:Cn lines (432 to 479) and the header.
- For the swap check: data/coverage.csv, data/modules.csv, data/modules/electives.txt and added.txt,
  docs/agents/gapfill/arts-health/codes.txt, docs/agents/catalog/tables/map-arts.md,
  docs/agents/decisions/DESK-ANSWERS.md, docs/reviews/arts-words-read-2026-11-20.md.
- For repeated picks: the visual arts, music, dance and theater frames of all four bands (searched by work and maker).
- The pilot read docs/reviews/frame-visual-arts-grades-k-to-2-2026-11-25.md, for REPEAT tags.
- Ran `python -X utf8 scripts/plan.py check`: all four media arts frames 0 failures (K-2, 3-5, 6-8: 60 unit days a
  year, 12 for checks and respond days; 9-12: 154 unit days a level, 24 for checks and respond days). Ran
  `python -X utf8 scripts/stale.py check`: 121 files, 0 failures.
- Nothing was fetched from the web; no downloads, no sign-ins.

## Verdict

**K to 2:** sound and close to adoptable; the one real fault is a check day that cannot run in 40 minutes with
kindergartners, plus two repeated picks with the theater and dance K to 2 frames. **3 to 5:** sound; the check days
are tight with no slack, and two works repeat the visual arts 3 to 5 frame. **6 to 8:** sound in structure, but its
claim that no work repeats an earlier media arts band is false (six works or makers repeat), and three making ids are
scored by written "what would you do" items instead of the work. **9 to 12:** the strongest of the four; its seams
note is stale (it says the 6 to 8 frame does not exist), and several works repeat 6 to 8 picks. The MA:Cn10 and
MA:Cn11 swap is complete and consistent in all four frames, the progression and the words file; only its record is
thin.

## Findings

Ranks: serious, moderate, minor, judgment call. LAYER is frame, progression, standard, base text or process. REPEAT
is yes (seen in an earlier read) or new.

### Serious

**S1. The K to 2 talk-and-table check day does not fit 40 minutes or one adult.** (LAYER frame, REPEAT yes, pilot
finding 3; likely)
What is wrong: the K to 2 check days run six groups of five at about 4 minutes a group, and the units 1, 5 and 9
checks give each kindergartner two talk items plus a safe-use table item: 15 spoken or handled responses in about 240
seconds, while 25 other five-year-olds wait unsupervised. The 3 to 5 check day (one talk item plus one table item in 3
minutes per five students) uses 40 of 40 minutes with no slack for set-up.
Why it matters: these checks are the evidence for owned ids; a check that cannot be run as written gets skipped or
faked, and the ids go unmet.
Fix: as the pilot fix, move the safe-use table item out of the check day into a rotating observation on the making
days (the guide's look-for, marked on a class list over the unit's last three making days), so the check day holds
talk items only. Give K-2 units 1, 5 and 9 a second check day or cut to one talk item a child; keep at least 5 minutes
of slack in every K to 5 check day, and state the waiting students' task (a quiet drawing card).

### Moderate

**M1. Works and makers repeat across the media arts bands, and the 6 to 8 frame says they do not.** (LAYER frame,
REPEAT new; firm)
What is wrong: the 6 to 8 frame states that no work "repeats a K to 2 or 3 to 5 media arts pick or maker". Repeats
found:
- McLaren and Lambart, Begone Dull Care: K-2 units 2 and 4, 6-8 unit 2, 9-12 unit 3 (four times).
- Muybridge, The Horse in Motion: K-2 units 1 and 7, 6-8 unit 8.
- de Chomón, El hotel eléctrico: 3-5 unit 5, 6-8 unit 1.
- McCay, Gertie the Dinosaur: K-2 unit 12, 6-8 unit 2.
- The Lumière brothers: K-2 unit 5 (Repas de bébé), 6-8 unit 1 (Workers Leaving the Lumière Factory).
- Ozu, Tokyo Story: 6-8 unit 3, 9-12 unit 4.
- Kahiu, Pumzi: 6-8 unit 10, 9-12 units 4 and 5.
- Te Wei, Where Is Mama: 3-5 unit 10, 9-12 unit 8.
- Same maker, new work: Méliès (3-5 Cendrillon, 9-12 A Trip to the Moon), Skawennati (3-5 CyberPowWow, 9-12
  TimeTraveller), Hopinka (6-8 Jáaji Approx., 9-12 Kicking the Clouds), Kunuk (6-8) and Isuma, which Kunuk co-founded
  (9-12).
The 3 to 5 frame's claim that no K to 2 maker repeats holds.
Why it matters: bar criterion on range across traditions; a student who walks the whole line meets the same few
early films three or four times while whole traditions (for example Latin American, South Asian and Arab media makers
below 6 to 8) stay thin. A false statement in a frame also misleads the unit-plan writer.
Fix: correct the 6 to 8 sentence. Swap the exact repeats in the later band for new picks that widen range (6-8 unit 1
de Chomón and Lumière, 6-8 unit 2 Begone Dull Care and Gertie, 6-8 unit 8 Muybridge, 9-12 unit 3 Begone Dull Care,
9-12 unit 4 Ozu and Pumzi, 9-12 unit 8 Where Is Mama), or keep at most one of them per band as a named revisit with
the harder question it now answers ("in K to 2 you saw it move; now you take its frames apart"). Same-maker, new-work
pairs may stay if named as revisits.

**M2. Works repeat between media arts and another arts frame of the same band.** (LAYER frame and process, REPEAT
new; firm)
What is wrong: a classroom teacher who teaches every art form in one band meets the same work twice in the same
grades:
- K to 2: kamishibai (theater K-2 units 1 and 2, kindergarten; media arts K-2 unit 3) and the Edison Annabelle
  Serpentine Dance film (dance K-2 unit 1, kindergarten; media arts K-2 unit 4).
- 3 to 5: Shaun Tan (visual arts 3-5 unit 2, grade 3; media arts 3-5 unit 1) and a Lakota winter count (visual arts
  3-5 unit 4, grade 3; media arts 3-5 unit 12).
- 9 to 12: Wangechi Mutu (visual arts 9-12 unit 3, The NewOnes; media arts 9-12 unit 10, a different work).
Cross-band only (lower weight): Lewis Hine (visual arts 3-5 unit 12, music 3-5 unit 1; media arts 6-8 unit 4),
Wendy Red Star (media arts K-2 unit 9; visual arts 9-12), Chaplin (theater 3-5 and 6-8 unit 1; media arts 6-8, The
Kid), Satyajit Ray (theater 9-12; media arts 6-8). Fodéba Keïta (dance 3-5) and Seydou Keïta are different people:
not a repeat.
Why it matters: the lens's "across the arts" check asks that the five disciplines be planned as one; same-band
repeats waste range and can read as an oversight to a reviewing teacher.
Fix: swap one of each same-band pair (the media arts pick is the easier swap in each case), or name the tie on purpose
in both frames ("the theater K to 2 frame tells this story live; here we see how the frames carry it"). Process fix:
frame-write's after-core section adds one check, "search the other arts frames of the same band for each named work
and maker", so the remaining arts frames do it at write time.

**M3. Three 6 to 8 making ids are scored by written items about what the student would do.** (LAYER frame, REPEAT
new; likely)
What is wrong: MA:Pr5.1.6c (show flexibility with tools), MA:Pr5.1.7c (adapt to a new purpose; the item asks "how the
student would adapt" to a purpose card) and MA:Pr5.1.8b (bend a convention; the item asks for "a convention the
student would bend") are each scored by a written item, not by work done.
Why it matters: the lens marks a written or vocabulary-style check against a making id as an assessment error; a
student can describe flexibility without showing it, and the id is about producing.
Fix: score each id as a guide look-for on the kept piece of its unit (the tool switch, the adapted cut, the bent
convention, each seen in the work) plus a one-line production-log entry naming it; keep the written item as practice
on the respond day. The K to 2 and 3 to 5 table items that show use are fine; 3 to 5's written comparison for
MA:Pr5.1.5c ("study") is fine.

**M4. The 9 to 12 seams note is stale.** (LAYER frame, REPEAT yes, pilot finding 5; firm)
What is wrong: the 9 to 12 Seams section says media-arts-grades-6-to-8 "has no frame yet", so its rows follow the
progression's assumes and hands_on cells. The 6 to 8 frame exists and its "Handed on to Media Arts, grades 9 to 12"
table agrees with the 9 to 12 rows. stale.py does not catch it (prose).
Why it matters: a reader trusts the note and goes to the progression instead of the frame.
Fix: rewrite the note to cite the 6 to 8 frame: ma-g8-read and ma-g8-society in its unit 9, ma-g8-ideas and craft in
unit 10, ma-g8-make and judge in unit 11, ma-g8-present and sources in unit 12, each with its days.

### Minor

**m1. The Cn10 and Cn11 swap is complete, but its record is thin.** (LAYER process, REPEAT new; firm)
What is right: in all four frames the unit id labels match their meanings (K-8: Cn11 in units 1, 5, 9; Cn10 in units
4, 8, 12; 9-12: Cn11 in units 2, 7, 12, Cn10 in units 5, 10, 15, both in unit 18), and so do the Devices bullets, the
course-level checks, the Sensitivity bullets on which units tie to the student's own life (Cn10), and the 6 to 8
cross-subject lean (ma-g8-society on computer science attribution). arts.csv ma-*-sources notes and words describe
own experience and sources, ma-*-society notes describe society, culture, ethics and tools. The words file reads
correctly. Every other MA:Cn use (coverage.csv, modules.csv, electives.txt, added.txt, gapfill codes, map-arts.md)
already matched the corrected meanings.
What is thin: the words-file header has no line recording the correction; DESK-ANSWERS has no entry; the 9 to 12
frame's For the lead has no swap item (the other three have it as item 1); and docs/reviews/arts-words-read-2026-11-20.md
passed the swapped file.
Fix (the lead's): one header line in ncas-performance-standards-words.txt ("2026-11-25: MA:Cn10 and MA:Cn11 lines
swapped back to their meanings, checked at the California CDE page"), one DESK-ANSWERS log entry, one sentence in the
9 to 12 For the lead, and a lessons line that a words read checks each id's meaning against a source page, not only
its wording.

**m2. K to 2 unit 9 meets only half of MA:Cn11.1.2a.** (LAYER frame, REPEAT new; likely)
The id names daily and cultural life, including media messages. The item checks the message and a place in daily or
community life only. Fix: add one look-for, "names a way the piece belongs to a family, cultural or community
tradition" (the unit's Wendy Red Star work already carries it).

**m3. The 6 to 8 screening day puts the self-check "that evening".** (LAYER frame, REPEAT new; firm)
That is homework, which Curio Class days do not assume. Fix: move the self-check into the next session's opener (5
minutes).

**m4. The 3 to 5 seam table's ma-g2-sources row lacks its unit and days in the cell.** (LAYER frame, REPEAT new; firm)
The note under the table explains it, but the table is what the checker and the unit planner read. Fix: put "K to 2
unit 12, days 179 to 192" in the cell.

**m5. The national weekly-time figure is Pending in all three K to 8 frames.** (LAYER standard, REPEAT new; firm)
STANDARD.md 3.4's media arts row is Pending. Fix: the lead approves the download of the visual and media arts
association's opportunity-to-learn checklists (elementary, middle, and high school if one exists), then the three
course pages name the figure. The 9 to 12 frame's choice to state no weekly figure and lean on the 120-hour level is
fine.

### Judgment calls

**J1. Deliberate revisits.** A work met at 6 and again at 16 can be good teaching. My pick: at most one named revisit
per work across the whole K to 12 line, always with the harder question stated in the later unit; four uses of Begone
Dull Care is too many.

**J2. The paper path for recording ids.** Every frame lets recording and producing ids be met on paper (flip books,
storyboards, shadow frames). That keeps the course free, and the ids say "media arts work", not "digital". My pick:
keep it, and let the course page say a shared device is welcome but never required. The money side is for Cory.

**J3. 9 to 12 For the lead item 1** (bridge and review units leave Skills empty and say None): agree with the pick, one
line in frame-write's after-core section.

## Settled by the expert

| Question | Answer | Basis |
|---|---|---|
| Which media arts connecting id is the student's own experience? | MA:Cn10 (a: own experience, interests, information and models; b: how media shapes meaning and culture). MA:Cn11 is daily, cultural and societal life (a) and tools, ethics and the legal setting (b). The swap back is right. | The lead's check at the California CDE page; matches the NCAS pattern in every other discipline (Cn10 personal, Cn11 society) |
| Do the four frames now use Cn10 and Cn11 consistently, including unit text? | Yes, every unit, check, Sensitivity bullet and cross-subject lean | Read in full, finding m1 |
| Can a making id be scored by a written "what would you do" item? | No; score the work, keep the writing as practice | Lens, assessment errors; M3 |
| Can K to 2 run a three-item talk-and-table check for five children in 4 minutes? | No | Finding S1, pilot finding 3 |
| Is the 6 to 8 "no repeats" claim true? | No; six works and four makers repeat | Finding M1 |

## Check-week clashes (listed, not counted)

- K to 2: week 27 meets theater K-2 (all grades), computer science K and 1, health, library K, ELD and PE (the frame's
  own For the lead item 3 says so). Week 21 is clear of arts.
- 3 to 5: grade 3 weeks 17 and 26, grade 4 weeks 17 and 25, grade 5 week 18 meet dance, theater or visual arts 3 to 5,
  and PE or SEL.
- 6 to 8: school day 83 (week 17), with health and PE on day 84; week 32 is finals.
- 9 to 12: weeks 16 and 32 in every level; the five arts 9 to 12 courses will likely all pick them (the frame's item
  3).
- Process note (pilot finding 2): the stagger check groups by subject, so arts-on-arts clashes in one classroom
  teacher's week are not flagged; the calendar pass should group the five arts.

## For Cory

- Supplies ceilings for a class of 30, each beside a free path, no device bought: K to 2 $75, 3 to 5 $50, 6 to 8
  $75, 9 to 12 $100 a class a level (provisional costs $90, $80, $80, $60 for Levels 1 to 4).
- Whether recording ids may be met fully on paper or whether a school should be told it needs one shared camera or
  tablet (a cost and audience question; J2).

## Downloads or sign-ins needed

- The visual and media arts association's opportunity-to-learn checklists (elementary and middle school, and high
  school if one exists), for STANDARD.md 3.4's Pending media arts row (m5). A download for the lead to approve.
- Nothing else; no sign-ins.

## Data checks

- **Owned skills:** every grade K to 8 has eight threads (ideas, make, craft, present, read, judge, society, sources),
  each owned by one unit; Levels 1 to 3 the same; Level 4 holds studio, exhibit, criticism and purpose on `~` Level 3
  ids. Unit Skills cells match the rows. Bridge and review units (9 to 12 units 1, 6, 11) own none, as STANDARD.md 3.2
  allows.
- **Standards in full:** 18 ids a grade K to 8, 54 a band, each claimed in its own grade only; 9 to 12 levels claim
  their own `.I`, `.II`, `.III` ids; no wrong-year id found (pilot finding 4 does not recur).
- **Units and reasons:** every unit has a question, a reason and id-by-id end-of-unit evidence (the pilot finding 1
  fix is carried in).
- **Days:** plan.py 0 failures for all four. Hand check: K-2 units 18, 22, 10, 10 a year; 3-5 sums by year match;
  6-8 14, 18, 14, 14; 9-12 Level 1 12, 30, 34, 38, 40, Levels 2 and 3 6, 32, 38, 38, 40, Level 4 48, 28, 40, 38; the
  once-a-week and short paths sum correctly (32 sessions, 80 days).
- **Seams:** answered at both ends with matching days, except the stale 9 to 12 note (M4) and one table cell (m4).
- **Cross-subject:** leans (ma-g3-judge on ela:SL.3.1, ma-g6-judge on ela:SL.6.1, ma-g8-society on computer science
  attribution) each carry an "if not yet" line; 9 to 12 leans on no course and its ELA, social studies and math
  contacts are practiced, not owned.
- **Lens checklist:** wrong-year ids none; all four processes every year; more than one tradition every year, with a
  Native maker each level, but range is narrowed by repeats (M1, M2); techniques get harder; daily period fits; a
  showing every year; technique taught first; words named; setting given on every work card; critique protocol
  named; revision built in; assessment by work except M3; no copied cornerstones; set-up and clean-up timed except the
  K-5 check days (S1); equipment and the paper path; safety (cables, lights, scissors) named; performing not solo-only;
  "respond" used correctly; no tool judges work; sacred works studied by looking only; family yes before any
  recording or showing.
- **Stale notes:** stale.py 0 failures; one stale prose note found by reading (M4).

## What is right and should not be touched

- Id-by-id evidence lines in every unit.
- The paper path and "media tool" read as anything that frames, captures, orders, plays or shows.
- The eight models (look-describe-interpret, media-ethics-check, storyboard, production roles, revision log,
  critique protocol, screening plan, source log) used from K and deepened each band.
- Family permission before any recording or showing, invented or public options on every Cn10 unit, sacred works by
  looking only, and the NFB films linked, never embedded or used as unseen items.
- The 9 to 12 level structure (bridge, reviews as placement, Level 4 series and defended statement).

## What could not be judged

- Dates, holders, living status and rights of the named works: from memory in the frames, to be checked on each
  holder's page at the unit plan (9 to 12 item 6). I did not fetch them.
- The national time figure (m5).

## Sources

- The California CDE media arts standards page for MA:Cn10, grade 3, as checked by the lead today (not refetched).
- National Core Arts Standards 2014, media arts, as held in data/standards/ncas-performance-standards-words.txt.

## For the source list

- The visual and media arts association's opportunity-to-learn checklists, once downloaded.

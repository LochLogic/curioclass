# Arts pre-work: stage 1 fix pass, 2026-11-20 (run 2026-11-21)

Read: the second-model read (docs/reviews/prework-arts-gemini-2026-11-20.md, findings 1 to 8 and its six questions,
the main list); the real-page findings of the two calibration reads as their scoring lists them
(docs/reviews/calibration-arts-2026-11-20.md, expert #9 to #12 and #14; docs/reviews/calibration-arts-gemini-2026-11-20.md,
Gemini #5, #9, #11, #12, #14 to #17); the arts parts of data/plans/later.csv L96; and the first reads
(docs/reviews/prework-arts-read-2026-11-19.md, docs/reviews/prework-arts-progression-read-2026-11-20.md) only to
avoid reopening a settled point. Settled calls read first: DESK-ANSWERS entries for q-later-arts-health-pe,
q-later-followups-1, q-prework-arts-1 and q-prework-open-1. Claims were checked against
data/standards/ncas-performance-standards.txt, the words file, data/progressions/arts.csv, scripts/progression.py and
UNIT-PLAN.md; the music "at a glance" handout (2021-11, the file's own source) was downloaded and read for the music
id claims. `python -X utf8 scripts/progression.py check arts`: 0 failures after the fixes.

## Findings

| Source | What | Decision | Where |
|---|---|---|---|
| gemini #1.1 | `MU:Re9.1.Kb` is a phantom: same words line as `.Ka` | Follow-up for the lead. Confirmed at source: the handout's kindergarten Re9.1 cell holds one statement (a). The id sits outside the header, so removal is the lead's; a header note now says so | ncas-performance-standards.txt header |
| gemini #1.2 | Music connecting should be `Cn10.0` and `Cn11.0` | Not a fault: the file's source handout prints `MU:Cn10.1` and `MU:Cn11.1`; the header now records the check | ncas-performance-standards.txt header |
| gemini #1.2 | Music connecting has the same words line in every grade | Fixed: the source repeats one statement each grade; STANDARD.md says so and where the change is told | STANDARD.md 3.1 |
| gemini #1.3 | `MA:Pr6.1.IIIb` words line over 14 words | Not a fault: 14 words by spaces, the hyphenated "personal-to-global" counted once | none |
| gemini #2.1, expert #14, gemini cal #14 | The progression's `grade` column for the levels (9, 10, 11, 12) is unstated | Fixed: the data key stated, never a student's grade | STANDARD.md 3.2 |
| gemini #2.2 | `~` carry of the year before's ids fails `code_grades` | Not a fault: practice that returns is not listed in a progression row, and a year claims only its own grade (3.1); one line now says rows list only their own ids | STANDARD.md 3.2 |
| gemini #2.3, gemini cal #14, progression read #14 | The 63 high school music strand ids are not loaded, so music 9 to 12 has no progression rows | Question for Cory (timing of a load the page sets for the frame) | Questions 1 |
| gemini #2.4, gemini cal #9 | Bridge unit "teaches the discipline's grade 8 ids" in 12 days, counted inside the 10 percent limit (15 percent of an 80-day path) | Question for Cory (rests on Desk q-prework-arts-1; what a course teaches) | Questions 2 |
| gemini #3, gemini cal #12 | APPROACH.md headings miss or mislabel UNIT-PLAN fields (fields 8 and 9 unmarked as section fields; no slot for unit field 6 or section field 4) | Fixed: every heading names its field; fields with nothing arts-specific are named once at the top | APPROACH.md, all headings |
| gemini #3 | Bar line "Section plan fills: the works studied and the showing" against unit field 2 | Follow-up for the lead (ADOPTION-BAR-SUBJECTS.md); the approach page is right, as ELA's text set sits in unit field 2 | Follow-ups 2 |
| gemini #3 | The baseline look on a unit's opening may read as a readiness check on day 1 | Fixed: it is an observation in the first practice days, not a readiness check | APPROACH.md "Readiness and the baseline look" |
| gemini #3, expert #9, gemini cal #11, L96 | Teaching first only in grades 2 to 5 | Fixed: every grade, pointing at UNIT-PLAN rule 13 | APPROACH.md "How a day opens" |
| gemini #3, gemini cal #12 | Safe use under supports (section field 9) | Fixed: moved to unit field 8, as science's safety | APPROACH.md "Tools, supplies and safe use" |
| gemini #3 | No one-projector line (FOUNDATION 5.1) | Fixed: one line, from the page's printed-version rule | APPROACH.md "Two rooms" |
| gemini #3 | Set-up and clean-up minutes not placed in the day row | Fixed: pointer to STANDARD.md 3.4 | APPROACH.md "How a day opens" |
| gemini #3 | Accommodations line, marking and response minutes, reading load in 6 to 12, ideal instrument | Not a fault: the shared UNIT-PLAN fields already require each; the page adds only what differs in the arts | none |
| gemini #3 | Family note content | Fixed in part: the family note is where the yes for an outside showing is asked; the leave-out notice waits on question 3 | APPROACH.md "Family note" |
| gemini #4, gemini cal #17 | Leans in STANDARD.md 6 name no core codes | Fixed: each bullet names the core codes its progression leans use, and points at the `cross_subject` column | STANDARD.md 6 |
| gemini #5.1, #5.2, #5.4, gemini cal #16 | 20 courses against five k-12 rows in data/courses.csv, `core = y` on visual arts and music, frame grain | Question for Cory (catalogue rows) | Questions 4 |
| gemini #5.3 | "the 15 high school courses" against 20 courses | Fixed: "15 high school levels (three in each of the five 9 to 12 courses)" | STANDARD.md 3.2 |
| gemini #6 | No minutes per lesson for 9 to 12; no national time figures named for K to 8 | Question for Cory (dose); the four figures are the reader's and were not checked at source | Questions 5 |
| gemini #7.1, #7.2 | Dance food and health ids, personal ties in Cn10, no reporting route | Question for Cory (sensitive ground; would bring health's and SEL's rules into the arts) | Questions 6 |
| gemini #7.3 | Sensitivity read limited to the works; safety read not wired | Fixed: every unit gets the sensitivity read, units with hands-on work the safety read, both in the brief | APPROACH.md "Works and their settings", "Safe use" |
| gemini #7.4 | Leaving out a whole unit "still meets the standards elsewhere" | Question for Cory (leave-out policy; the Desk entry does not say the standards are met elsewhere) | Questions 3 |
| gemini #8.1 | DRAFT banners after the approach yes | Fixed: approval and date on APPROACH.md; STANDARD.md status names the Desk cards that settled it | APPROACH.md, STANDARD.md top |
| gemini #8.1 | Lens and bar row still say draft and "Cory, then agent" | Follow-up for the lead | Follow-ups 3 and 4 |
| gemini #8.2 | Sources table misses the March 2026 update, the high school review and a from-memory row | Fixed | APPROACH.md "Evidence and sources" |
| gemini #8.3 | Unseen work defined for dance and theater only | Fixed: visual arts, music and media arts use a public domain, openly licensed or Curio Class work | APPROACH.md "Scoring creative work" |
| gemini #8.4 | "colour" beside "color" | Fixed: "color" | APPROACH.md "Tools, supplies and safe use" |
| expert #10 | Scoring spread across the check day and the respond day, so the respond day cannot act on every mark | Fixed: groups show on the check day, any not watched live are recorded that day, marks are in before the respond day | APPROACH.md "Scoring creative work" |
| expert #11 | The 32-session path keeps no study of a work, so responding and connecting drop out | Fixed: the demonstration day opens with the look or listen at a work, still four days | STANDARD.md 3.4 |
| expert #12 | Connecting placed only in a study day's sentence, though many Cn ids ask for making, research or performing (`VA:Cn10.1.Ka`, `DA:Cn10.1.6b`) | Fixed: each Cn id is taught as its words line asks, ties on the study day, making on an application day | APPROACH.md "Kinds of day" |
| gemini cal #5, L96 | mu-g5-respond never teaches `MU:Cn11.1.5a` and drops the music-element evidence of `MU:Re9.1.5a` | Fixed | arts.csv mu-g5-respond |
| gemini cal #15 | mu-g4-perform and mu-g5-perform lack the solo-or-doubled note; mu-g5-revise drops "how it shows intent" | Fixed (swept the music perform rows: only grades 4 and 5 name solo performing in their ids) | arts.csv mu-g4-perform, mu-g5-perform, mu-g5-revise |
| progression read, for Cory 2 | Leave out a sacred or ceremonial unit? | Settled, no change: Desk q-prework-open-1, already in STANDARD.md 5 | none |
| progression read #10, #13 | Own yes at 18; fair use | Not a fault: both already applied in arts.csv | none |
| first read #9, #12, #15, #16, #20 | Overlaps with gemini #3, #4, #7.4, #8.2 | Handled under those lines | as above |
| first read, for Cory 1 to 4 | Own-words file, short path, leave-out per course page, approach yes | Settled, no change (Desk q-prework-arts-1) | none |

Counts: fixed 21, not a fault 5, settled with no change 2, questions for Cory 6, follow-ups for the lead 4.

## Questions for Cory

1. **Load the 63 high school music ids now?** STANDARD.md loads them by hand when the high school music frame is
   written, so data/progressions/arts.csv has no music rows for grades 9 to 12 and the stage 2 check cannot see that
   course. Pick: load the ids and their words lines now, then add the music 9 to 12 rows, so the progression covers
   all 20 courses before stage 3.
2. **What the Level 1 bridge unit teaches, and how its days count.** STANDARD.md 3.2 says the bridge (at most 12
   days) "teaches the discipline's grade 8 ids" (15 to 24 ids) and counts as inside the standards for the bar's 10
   percent limit; 12 days is 15 percent of the 80-day path. Pick: the bridge teaches the grade 8 techniques and words
   Level 1 needs as readiness, claims no grade 8 id, and shrinks to 6 days on the 80-day path.
3. **Leaving out a whole unit.** STANDARD.md 5 says a left-out unit's standards "are still met elsewhere in the year",
   which holds only if every id is taught twice. Pick: as SEL, swapping a work keeps the ids met; leaving out a unit
   means the course page and the unit's family note name the ids not claimed that year.
4. **Arts rows in data/courses.csv.** The pages count 20 courses (five disciplines by four bands); the catalogue has
   five k-12 rows, with `core = y` on visual arts and music. Pick: 20 band rows, all `core = n`, as SEL, ELD and
   health were split (later.csv L90).
5. **High school minutes and the national time figures.** 9 to 12 states 160 days but no minutes (C2); 45 minutes
   gives the 120 hours the level descriptor names. The reader quoted four associations' recommended weekly times for
   K to 8, not checked at source. Pick: 45 minutes for 9 to 12; the course pages name each association's figure and
   the gap, as health does, once the figures are read at source.
6. **Health and SEL's guardrails in the arts.** Dance ids `DA:Pr5.1.4b` to `.IIIb` ask about food choices and
   one's own health habits and eating plan (only the Level 2 row has a note), Cn10 ids ask for ties to the student's
   own life, and the pages give no route if a student discloses harm. Pick: bring in health's rule (no task asks about
   a student's own diet, weight or body), an invented or public option beside every personal-tie task, and SEL's
   reporting-route teacher note.

## Follow-ups for the lead

1. Remove `MU:Re9.1.Kb` from data/standards/ncas-performance-standards.txt (line 701) and from
   data/standards/ncas-performance-standards-words.txt (line 636), and from row mu-k-respond in
   data/progressions/arts.csv; drop its header note; then update STANDARD.md (section 1: 1,201 ids, music 201;
   section 3.2: music K 18, K to 2 18 + 20 + 20 = 58, 1,113 taught, music 184, "music K 18").
2. docs/ADOPTION-BAR-SUBJECTS.md arts "Section plan fills: the works studied and the showing" to "Unit plan fills
   (field 2): the technique, the works studied and the showing", matching APPROACH.md.
3. docs/agents/lenses/arts.md line 5: "APPROACH.md (draft)" to "(approved 2026-11-20)".
4. docs/ADOPTION-BAR-SUBJECTS.md arts row of the owed table: "Who" still reads "Cory, then agent"; add "stage 1
   second-model read and fix pass (docs/reviews/prework-arts-fixes-2026-11-20.md)" as the health row does.

All four follow-ups done by the lead 2026-11-21: MU:Re9.1.Kb removed from the id file, the words file and mu-k-respond, with STANDARD.md counts updated (1,201 ids, 1,113 taught); the bar line and owed row and the lens line fixed. The six questions are on the Desk (q-fix-arts-1).

## Answers applied (Cory, 2026-11-21, Desk q-fix-arts-1)

1. Load the 63 high school music ids now: decided, held. The strand is published at source only as files to download
   (nationalartsstandards.org/sites/default/files/2021-11/Music%20Theory%20and%20Composition%20Strand%20at%20a%20Glance.pdf;
   nafme.org/wp-content/uploads/2023/04/2014-Music-Standards-Composition-Theory-Strand.pdf), and the coalition's
   customize-handbook page reaches it only through a form, so nothing was loaded and no music Level 1 to 4 rows were
   added. STANDARD.md 1 and 3.3 state the decision, with a Pending marker on the load; counts stay 1,201 ids, 1,113 taught.
2. Bridge unit: STANDARD.md 3.2 (readiness, no grade 8 id, 6 days on the 80-day short path, counted toward the 10
   percent limit); the four Level 1 rows in arts.csv (va-g9-ideas, th-g9-imagine, da-g9-ideas, ma-g9-ideas) say the same.
3. Leave-out: STANDARD.md 5 (swap keeps the ids; a left-out unit's ids are named on the course page and in the
   unit's family note); APPROACH.md "Family note" points there.
4. Catalogue split (done by the lead): STANDARD.md names the 20 course ids, none core.
5. High school minutes: STANDARD.md 3.4 (45 minutes, 120 hours; 60 on the short path) and the rule for national
   time figures. No association's weekly figure could be read by page fetch (the music, visual and media arts,
   dance and theater opportunity-to-learn standards are files to download), so none is named.
6. Sensitive ground: new APPROACH.md "Sensitive ground" section (diet, weight and body; an invented or public option
   beside every Cn10 personal tie; health's steps for when a student tells you something). Progression notes for
   da-g4-technique to da-g11-technique carry the teacher note; the grade 8, Level 1 and Level 2 wording no longer
   asks for the student's own food or eating plan.

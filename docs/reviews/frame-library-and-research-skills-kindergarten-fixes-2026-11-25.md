# Frame fixes: Library and Research Skills, kindergarten, 2026-11-25

The one fix pass of COURSE-RUN stage 3 for the library pilot frame
(docs/courses/library-and-research-skills-kindergarten/frame.md), from the expert read
(docs/reviews/frame-library-and-research-skills-kindergarten-2026-11-25.md, E) and the second-model read
(docs/reviews/frame-library-and-research-skills-kindergarten-codex-2026-11-25.md, C). Files changed: the frame,
data/progressions/library.csv (three K row notes, LF endings kept), docs/courses/library/APPROACH.md and STANDARD.md,
and frames.csv, calendar.csv and CALENDAR.md through sync.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses; calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check library-and-research-skills-kindergarten` | 0 failures; 4 units, 30 days (24 in units, 6 for checks and respond days) |
| `python -X utf8 scripts/progression.py check library` | 98 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |

Days now: unit 1 6 (weeks 1 to 6), unit 2 6 (7 to 12), mid-year check 1 (13) and respond 1 (14), unit 3 5 (15 to 19),
unit 4 7 (20 to 26), year-end check 2 (27, 28) and respond 2 (29, 30). Check weeks did not move.

## Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| E | 1 | Applied | The Days bullet states 19 working minutes and one adult in the room. The Evidence bullet defines three costed forms (circle round about 30 seconds a child; whisper walk; station of three to five at about 2 to 2.5 minutes a group) plus a scanned pointing item, and bars any spill into a respond day. Every unit's evidence and both check rows give their form and total for 30 (10 to 17 minutes). "A class of up to 24" is gone |
| E | 2 | Applied | Mid-year samples unit 1 (wonder and the cycle) on a new case. Year-end samples units 1 to 3 on new cases. The unit just ended (2, then 4) is reused unscored as a class count on the check sheet. I did not keep a per-child checklist past its unit as E proposed, because a class count meets lesson 20 and the APPROACH.md K to 2 rule (thrown away at unit end) stays as approved |
| E | 3 | Applied | Unit 1's evidence adds pointing at the four cycle pictures in order (k-class-inquiry). Unit 2's adds putting the book back in its bin and pointing at the three stop pictures in order (k-library-visit). The k-library-visit row note now says what K checks (both ends) |
| E | 4 | Applied | Unit 2 goes to 6 days: show-me (care, borrowing, stop rule), show-me (bins, story or fact), practice, inquiry, assessment, respond. Unit 1 goes to 6 days, with its share opening the respond day as unit 3's does. The load sentence is rewritten (two-row units get 6, 6 and 7 days, the one-row unit 5). Both reads agreed on unit 1 at 6 days |
| E | 5 | Partly applied | Rejected: a one-session year-end check. E's own forms do not fit it: three items take a circle or whisper form (about 15 minutes) plus a station (about 15 minutes), more than 19. Applied: the two check days now carry that reason, and respond day 2 is stated as the year's reflect step, not as a week filler. Teaching days are 16 of 30, not E's 18, because the year-end needs its second session |
| E | 6 | Applied | Placement names the week 27 (computer science, health) and week 28 (ELD, physical education) clashes. The stagger question is For the lead item 4. No week moved (this pass's rule) |
| E | 7 | Applied | The stale frame.py item is removed; frame.py already reads "every two weeks" as 0.5. The band-frame facts (Year column, 18 days a year) are in the pattern notes below, since the brief and APPROACH.md already state them |
| E | 8 | Applied | The guidance is named by title with a free link: "Be Safer Online with NetSmartz: Grades K-2", https://www.missingkids.org/netsmartz/resources (listing read 2026-11-25; the kit was not opened, and downloads may need a sign-in). The vague second clause is dropped, since unit 2's own borrowing rule stands. A line says no organization's name goes on a student, teacher or family page |
| E | 9 | Applied | The inquiry arc bullet now maps judge (choosing the fact book at find, unit 2) and use (drawing the found fact) onto the four pictures |
| E | 10 | Applied | Checked at the band file: the K construct cell is sorting things and information; "sorts books by fiction vs. nonfiction" is the grade 1 cell. The k-picture-book-labels note now says so, and the frame's L103 record is corrected |
| E | 11 | Applied | Unit 1 asks "What do we wonder about, and how can we find out?", with seeds as the stand-alone case and the host's wonder (for example, push-pull) answerable too |
| C | 1 | Partly applied | Applied: each unit plan shows its full 19-minute budget, and no assessment overflows into a respond day. Unit 1 goes to 6 days. Rejected: a two-session mid-year check in weeks 12 and 13, with unit 2 at 5 days. The new mid-year form (one combined circle turn, about 15 minutes) fits one session. The freed day goes to unit 2, which both E4 and C2 show is short. Also rejected: observation windows on inquiry days, since lesson 19 wants unseen items on the scored day and the costed forms now fit it |
| C | 2 | Applied | Unit 2's question is now "How do we find a book that answers our question, and look after it?". It has a real inquiry: find the labeled bin, pick the fact book over the story book, the teacher reads a rain passage, each child draws one fact, a partner share, and the self-check. "Which bin holds the rain book?" is the find-step prompt. The stand-alone question is "What happens when rain falls?". The Inquiry phases cell adds express and reflect |
| C | 3 | Applied | Same as E7 |

L103, kindergarten row fixes (frame items 7 to 9 and E10), now in data/progressions/library.csv:
- k-library-visit: the K private-information cell is taught in grade 1 (g1-device-stop-rule).
- k-picture-book-labels: picture or color labels instead of ABC order, which comes in grade 2 with g2-catalog-lookup. The fiction and nonfiction book sort is the continuum's grade 1 cell, done here with help.
- k-who-made-book: telling a found fact from one's own idea is said aloud here.

The frame's L103 result moved from For the lead into a "Check set read" bullet in The course in brief.

Other stale notes fixed:
- APPROACH.md: "judgement" becomes "judgment" (5 places), the US spelling L103 asked for. "Questions in this draft" becomes "Settled questions", since every item there is settled.
- STANDARD.md: the owed-row cell now says the grades 3 to 5 band was read from the web and has no copy in the store.
- Frame For the lead items 1 (dose), 2 (gate wording), 3 (check-week method) and 11 (3 to 5 file) moved to the pattern notes or to For Cory below.

## Pattern notes for the other library frames

- Cost every assessment against the working minutes for a class of 30, by form: circle round (about 30 seconds a child), whisper walk (when neighbors could copy), station (others on a practiced book-corner task), or scanned pointing. No spill into respond days.
- Course-level checks sample earlier units on new cases. The unit just ended is reused unscored as a class count, so no per-child record outlives its unit.
- Every row gets a scored item somewhere in the year. Two-row units get at least 6 days. Every unit, unit 2's kind included, ends in a drawn or spoken product, a share and the self-check.
- Compelling questions stay topic-open, so the host or the stand-alone case can answer them.
- Placement names after-core clashes as well as core weeks. Check weeks stay put until the lead's calendar pass. Grade 2's year-end check must sit by week 27 (core science is week 28).
- Dose: grades 1 and 2 take 30 sessions of 25 minutes, grades 3 to 5 30 sessions of 35 minutes (APPROACH.md). The 6 to 8 and 9 to 12 frames keep "about one session every two weeks" (frame.py reads 0.5 a week), use the Year column, and run 18 days a year (54 and 72).
- Keep the L103 record as a Check set read bullet, with each difference written into the row note in the same pass.

## Left for the lead

- After-core check stagger: K weeks 27 (computer science, health, library) and 28 (ELD, library, physical education). The same run also shows grade 1 week 28 (ELD, physical education) and grade 2 week 27 (ELD, health, physical education). This is for the one calendar pass.
- The brief's after-core section: name "Inquiry phases" as library's C3 column, and allow an empty Owned standards cell for carry-only units (frame items 1 and 2).
- ELA K unit 3 plan: use the same four cycle words, ask, find, share, reflect (frame item 3).
- later.csv L103: mark kindergarten done. The APPROACH.md spelling clause is now done. The row stays open for grades 1 to 12.
- The library lens (docs/agents/lenses/library.md) has UK spellings: "catalogues", "licences", "licence", "judgement". That file is outside this pass.
- No DESK-ANSWERS line is needed: no rule doc changed meaning. The check-record choice kept the APPROACH.md rule as approved.

## For Cory

- Download the continuum's grades 3 to 5 band file into S:\CurioClass-sources\library\aasl-2026-11-21. L103 needs it before the grade 3 frame. Your 2026-11-21 yes (Desk q-fix-library-1, "the continuum band files") may already cover it; please confirm.

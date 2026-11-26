# Frame fixes: Visual Arts, grades K to 2 (2026-11-25)

The one fix pass of COURSE-RUN stage 3 for the after-core arts pilot frame
docs/courses/visual-arts-grades-k-to-2/frame.md, from the expert read
(docs/reviews/frame-visual-arts-grades-k-to-2-2026-11-25.md, "E") and the second-model read
(docs/reviews/frame-visual-arts-grades-k-to-2-codex-2026-11-25.md, "C").

Files changed: the frame; data/progressions/arts.csv (16 note and description edits in 15 va K to 2 rows, LF kept);
docs/courses/arts/STANDARD.md (section 1 and 3.4, CRLF kept); data/plans/frames.csv, data/plans/calendar.csv and
docs/courses/CALENDAR.md through `frame.py sync`.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses, calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check visual-arts-grades-k-to-2` | 0 failures; unit days K 60, 1 60, 2 60; 192 days (180 in units, 12 for checks and respond days) |
| `python -X utf8 scripts/progression.py check arts` | 498 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |

## Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| E | 1 | Applied, with one item changed by C1 | Every unit's evidence is now written id by id ("End-of-unit evidence, id by id: ..."), each id with a talk item, a table item, a guide look-for or a kept card. New brief sentence in Scored evidence: every owned id has an item or a look-for, and a row's "Assessed by" note is never the whole line. Mid-year checks now name only the ids their tasks test (Re7.1.1a and Re7.1.2a out of the year 1 and 2 checks; year K keeps Re7.1.Ka with a new use-of-art item). E's unit 1 item ("name two places where you saw art") was replaced by C1's use item, settled by the national standard's text. |
| E | 2 | Applied in part (by the job's rule) | Check weeks not moved: the lead runs one calendar pass over all after-core frames (job instruction, CALENDAR.md rule 1). For the lead item 3 (the arts-only stagger with weeks that clash with SEL, health, computer science and library) is dropped; the clashes, the free weeks and the subject-key point are now For the lead items 1 and 2. Checks stay off every core check week. |
| E | 3 | Applied, adjusted to APPROACH | Not moved to making days: APPROACH "Kinds of day" says the end-of-unit assessment is always a check day. Instead the check day is one job: the showing is scored from kept work after the session, and the safe-supply or safe-handling item is done at the teacher's table inside each group's four minutes. Minutes stated in the brief: set-up 5, self-check 5, six groups of about 4 (24), clean-up 4, 38 in all; no paint or clay on a check day; at most two talk items a child. |
| E | 4 | Applied | VA:Cr2.2.Ka is now a safe-supply pick (tray of items or picture cards, labeled non-toxic against unlabeled, blunt-tip against sharp), in unit 1 and the year K mid-year check; handling is practice, named as grade 1's id. va-k-craft's "Assessed by" note changed to match (and "labelled" to "labeled"). |
| E | 5 | Applied | Standard bullet now says scripts/standards.py checks every id (L83 done 2026-11-21). Old For the lead item 4 dropped. STANDARD.md section 1 rewritten as done. The ADOPTION-BAR-SUBJECTS.md arts row is a shared doc outside this job's files: For the lead item 4 with the replacement. |
| E | 6 | Applied | Once-a-week bullet: check sessions in the full path's weeks, respond sessions one week later (weeks 19 or 18, and 27), not check weeks. Arithmetic re-checked (year K and 1: 9 + 8 sessions, check 18, respond 19; year 2: 8 + 8, check 17, respond 18; year-end check 26, respond 27). |
| E | 7 | Applied | "four kindergarten threads" now "eight". |
| E | 8 | Applied | Unit 3 uses the museum's title "Woman on a Bridge #1 of 5: Tar Beach" with accession 88.3620. Unit 11's last cell has the liquor-cap teacher note and the Met page the agent reads first. |
| E | 9 | Applied | Year K gains Esther Mahlangu, Ndebele Patterns (South Africa, 2015, LACMA, object 285405) in unit 1, which also fits the use-of-art demand (painted house walls). Unit 7 gains a black-on-black jar by Maria Martinez and Julian Martinez (San Ildefonso Pueblo, the Met, 736324), with a sensitivity note (no avanyu design, Pueblo source read first, no copying). Unit 10 gains Lygia Clark (Brazil). Candidate cells updated so they no longer ask for what is now picked. |
| C | 1 | Applied (frame and row); words line to the lead | Checked against the NCAS kindergarten standard (uses of art nearby; noticing art is pre-kindergarten). Unit 1's question, learning line, words ("use" for "see"), evidence and the year K mid-year check now teach and check the use. va-k-look's description and "Assessed by" changed. The words file (data/standards/) is outside this job's files: For the lead item 3 with C's replacement line. |
| C | 2 | Applied | Merged with E1. C's unit-specific points all landed: unit 1 experiment sheets as a look-for; unit 4 portfolio purpose and museum-against-building sort; unit 7 visible groups by use, the pot beside them, not in place of them; unit 8 prize talk, exhibit-plan card, job-card sort, reasons for both works; unit 9 a looking-walk place item; unit 12 a display-materials card and a likeness and a difference between the two cultures. Progression "Assessed by" notes changed for the 14 rows whose template was narrower than their ids. |
| C | 3 | Applied | Read at source 2026-11-25: the association's elementary checklist, page 3 ("a minimum of one 50-minute art class per week") and page 4 ("at least 50 minutes weekly", taught by a certified visual arts educator). The Days bullet now states the figure and the gaps (30 over; 10 short on the once-a-week path). STANDARD.md 3.4 row split: visual arts K to 5 carries the figure; visual arts 6 to 8 and media arts wait on their own documents (For the lead item 5). |
| C | 4 | Applied | Unit 2 revisits Hokusai beside Kandinsky; unit 4 names Annie Mae Young's 1976 strip-medallion quilt (the Met, 654092) and revisits Tar Beach; unit 10 names Asawa's Untitled (S.270 ...) at the Whitney (works/2260) and adds Lygia Clark's Bicho (1960, the Walker). |
| C | 5 | Applied | Same stale notes as E5 (rows 1 to 3 of C's table). Row 4: the real clashes are named in For the lead item 1. |

Counts: 14 findings (E 9, C 5); 14 applied, 3 of them in part or adjusted (E2 by the job's calendar rule, E3 by
APPROACH, E1's unit 1 item by C1); 0 rejected outright.

Also fixed while editing: "practised" and "practise" to US "practiced" and "practice" (AGENTS.md); unit 2's partner
note now keeps the child working with the partner (Cr1.2.Ka asks for work with others); the old For the lead items
1, 2, 6 to 10 (pattern picks for other frames, and a model name with no change asked) moved to the pattern notes
below.

## Pattern notes for the other arts frames

Copy:
- The id-by-id evidence line in every unit ("End-of-unit evidence, id by id: <id>, <item kind>: <item>; ..."), and
  the Scored evidence sentence that every owned id has an item or a look-for. Never copy a row's "Assessed by" note as
  the unit's evidence: it names one form per row.
- Three item kinds: a guide look-for scored from kept work after the session; a kept card or sort made on the last
  making days; talk or table items at the teacher's table, at most two talk items a child. State the check day's
  minutes (set-up, self-check, groups, clean-up) inside the session; no paint or clay on a check day; one adult
  watches one table.
- A course-level check names only the ids its task tests.
- Check each id's action against its national standard text, not only the words file: a words line can drift to the
  grade below (VA:Re7.1.Ka did).
- Read each discipline's national time figure in the grade band's own opportunity-to-learn document (elementary,
  middle, high), and state the gap on both paths.
- Name every work exactly (the holding museum's title and link); two to four works by other artists a unit, a
  revisit of an earlier unit's work allowed; range-check across the band, not only within a year (Africa, the
  Americas including Native American makers, Asia, Europe; living makers each year).
- From the pilot, unchanged: the Year column and units numbered through the band; the four-unit year with two
  threads a unit in the same slot each year where the rows pair that way; the "Processes, anchors and works" C3
  heading; the exhibit or performance unit last, assessed by its own showing, after the year-end check; the
  once-a-week counts per unit; the four-line logic model; the safety bullet with its two guides; the leave-out and
  sensitivity bullets naming units and communities.

Avoid:
- Copying weeks 17, 18 or 26, or any arts-only stagger: wait for the lead's after-core calendar pass.
- Scoring a performance check on the check day while also hearing talk groups.
- Any "until the standards gate exists" line: scripts/standards.py checks ids now.

## Left for the lead

1. After-core clashes this frame is in (checks stay off core weeks; weeks not moved): grade K week 18 (arts, ELD,
   physical education), grade K week 26 (arts, SEL), grade 1 week 18 (arts, ELD, physical education), grade 1 week
   26 (arts, SEL), grade 2 week 17 (arts, ELD, physical education), grade 2 week 26 (arts, SEL). Free of every check
   in K to 2 today: weeks 1 to 8 and 21 to 25.
2. frame.py's stagger check keys on subject, so two arts disciplines in one week are never flagged; key it on course
   for the arts.
3. data/standards/ncas-performance-standards-words.txt line 1116 (VA:Re7.1.Ka): replace with "Identify what nearby
   art is used for, with examples from your surroundings."
4. docs/ADOPTION-BAR-SUBJECTS.md, arts row of "Before a scope and sequence": drop "Owed: the standards gate (later.csv
   L83)" and the high school music strand load (both done 2026-11-21).
5. Read the visual arts educators' association's middle school checklist
   (arteducators.org/wp-content/uploads/2025/09/OTL-Middle_School_Visual_Media_Arts_Program.pdf) and its media arts
   lines at source, then fill the Pending row in STANDARD.md 3.4.

## For Cory

- Money: the K to 2 visual arts supplies ceiling. Provisional costs $70, $50 and $40 a class of 30 a year, all
  optional beside a free path; the frame's pick is $75 a class a year.

## Sources read for this pass

- https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Elementary_Visual_Media_Arts_Program.pdf : pages 3 and
  4, the 50-minute weekly figure.
- https://collections.lacma.org/object/285405 : Mahlangu, Ndebele Patterns, 2015 (from a search listing; the unit
  plan opens the page for the rights line).
- https://metmuseum.org/art/collection/search/654092 : Annie Mae Young's 1976 quilt (from a search listing).
- https://metmuseum.org/art/collection/search/736324 : Maria Martinez and Julian Martinez, Black-on-Black Jar (from a
  search listing).
- https://whitney.org/collection/works/2260 : Asawa, Untitled (S.270 ...), dated 1955 on the page (a video caption
  gives 1954; the unit plan records the page's date).

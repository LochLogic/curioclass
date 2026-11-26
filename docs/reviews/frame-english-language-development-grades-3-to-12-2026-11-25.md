# Frame read: English Language Development, grades 3 to 5, 6 to 8 and 9 to 12, 2026-11-25

Expert frame read (COURSE-RUN stage 3) of the three ELD band frames written after the K-2 pilot. Read only; this
report is the only file changed.

## What was read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/frame-read.md, frame-write.md ("After-core courses"),
  docs/agents/lenses/eld.md, docs/courses/eld/STANDARD.md, docs/courses/eld/APPROACH.md,
  docs/ADOPTION-BAR-SUBJECTS.md part 10 (items 1 to 14 and "Fails if").
- The K-2 pilot read and its fixes file (docs/reviews/frame-english-language-development-grades-k-to-2-2026-11-25.md,
  -fixes-2026-11-25.md), and the K-2 frame's talk routine, newcomer strand and handed-on table (seam checks).
- The three frames in full:
  docs/courses/english-language-development-grades-3-to-5/frame.md,
  docs/courses/english-language-development-grades-6-to-8/frame.md,
  docs/courses/english-language-development-grades-9-to-12/frame.md.
- data/progressions/eld.csv (rows from each course's `rows` cell in data/plans/course-list.csv: grade:3|4|5,
  6|7|8, 9|10|11|12), data/standards/wida-2020.txt, data/plans/calendar.csv, data/plans/frames.csv, and every named
  host frame's Units table (ELA, math, science, social studies, grades 3 to 12) through scratch scripts that compared
  host unit days, course days to school days, and the skill ids each ELD row cites.

## Gates

| Gate | Result |
|---|---|
| `frame.py check english-language-development-grades-3-to-5` | 0 failures; 154 unit days in each of grades 3, 4, 5 (480 days with checks) |
| `frame.py check english-language-development-grades-6-to-8` | 0 failures; 154 each year (480) |
| `frame.py check english-language-development-grades-9-to-12` | 0 failures; 154 each year (640) |
| `progression.py check eld` | 162 rows, 0 failures |

`stale.py check` fails only on other courses' files (physical education 6-8 and 9-12, theater 6-8), which are being
written at the same time; not a finding.

## Verdict

All three frames are sound and adoptable after small fixes: every unit has one host cited by course days, every
owned WIDA id is valid and owned by the right grade, every cited skill sits in the named host unit, days follow host
windows first, and checks sit off core check weeks (grades 6 to 12 year-end in finals week 32). The pilot's fixes
are mostly carried; the gaps are the unseen-text search rule in 6-8 and 9-12, the framework printed-list check still
not done in any band, and three units (3-5 unit 18, 6-8 units 1 and 18) that host on migration, war or loss without
the family-note preview STANDARD section 3 asks for. The rest is stale lead notes and wording.

## Findings

Severity counts: 0 serious, 3 moderate, 13 minor, 1 judgment call.

### 1. Moderate. Unseen-text picks not checked across docs/ and data/ (6-8, 9-12; partly 3-5)

- Course: 6-8 and 9-12 (3-5 has the rule). LAYER: frame. REPEAT: yes (pilot E3). Confidence: high.
- What is wrong: only the 3-5 frame says the unit writer searches docs/ and data/ (section plans and items.csv too)
  before writing new content. 6-8 and 9-12 do not. 9-12 also names unseen "public-domain selections" for end-of-unit
  tasks without picking them, in units 17, 20, 22, 24, 28 and 33, while ELA 9 to 12 and US History already use
  founding-era speeches and essays.
- Why it matters: an "unseen" text a student has already read in ELA or history tests memory, not transfer, and the
  bar's assessment items assume unseen.
- Fix: add to the Base text bullet of 6-8 and 9-12: "Every text named as unseen is checked unused in docs/ and data/
  (section plans and items.csv too) before it is written in." In each 9-12 "selection" unit add "checked unused in
  docs/ and data/ before use".

### 2. Moderate. Owned ids not yet checked against the framework's printed lists (all three)

- Course: 3-5, 6-8, 9-12. LAYER: standard and process. REPEAT: yes (pilot C1 and its pattern note, which asked for
  this before the frame read). Confidence: high that it is not done; the content itself I could not judge.
- What is wrong: each frame teaches "every part" of its owned ids in its own words (3-5 For the lead item 7, 6-8
  item 2, 9-12 item 2) but says the printed lists in the WIDA 2020 framework were not opened. The 3-5 frame calls it a
  "browser check", but the PDF is not blocked; it simply was not opened.
- Why it matters: bar item 2 (ids taught in full). The pilot found missing parts only by reading the printed pages.
- Fix: the lead (or a run with permission to download) opens the free framework
  (https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf) at the 2-3, 4-5, 6-8,
  9-12 and SI expectation pages, and edits the "every part" sentences in each owned unit and its row note in place.
  In 3-5, reword "browser check" to "not yet opened".

### 3. Moderate. Hosts on migration, war or loss without the family-note preview (3-5 unit 18, 6-8 units 1 and 18)

- Course: 3-5, 6-8. LAYER: frame. REPEAT: new. Confidence: high.
- What is wrong: STANDARD section 3 says a host about migration, war or loss carries a family note that previews the
  topic and says how to ask for the other text. 3-5 unit 18 (a father's death, losing the home, moving for farm
  work), 6-8 unit 1 (a flood and a choice about moving) and 6-8 unit 18 (loss in the Civil War, a parent living
  apart) do not. 6-8 unit 17 and 9-12 units 1, 8, 11, 13, 18, 19, 23 and 24 do it right.
- Why it matters: newcomers and refugee students are the course's own audience (lens, trauma-informed line).
- Fix: add to each of the three units: "The family note previews <topic> and says how to ask for the other text
  (<the other chapter or text the host names>)."

### 4. Minor. "incertidumbre is not a cognate of uncertainty" (9-12 unit 35, row g12-sc-argue)

- LAYER: frame and progression. REPEAT: yes (pilot E12). Confidence: high (both from Latin certus).
- Fix: "incertidumbre and uncertainty share a root but look different, so the word card carries it", in the unit row
  and the g12-sc-argue note.

### 5. Minor. Stale For the lead items (3-5 items 2, 8, 9)

- LAYER: process. REPEAT: yes. Confidence: high.
- What is wrong: item 2 says "progression not edited", but the six cognate notes are in eld.csv (commit 543dba40b:
  fuerza, cuadrado, capítulo, razón, ejemplo, señal). Item 8 (señal) is applied; g11-sc-explain says "share a root".
  Item 9 points at a 6-8 Pending line and an ELD stale failure that no longer exist.
- Fix: rewrite item 2 as "Applied in eld.csv (543dba40b)"; remove items 8 and 9.

### 6. Minor. Stale Pythagorean lean (6-8)

- LAYER: process. REPEAT: yes. Confidence: high.
- What is wrong: the cross-subject grade 8 math table still lists m8-pythagorean-theorem as a lean of g8-ma-argue;
  the row now leans on m8-congruence and m8-angle-facts. For the lead item 3 says "(below)" with nothing below;
  item 5 counts m8-pythagorean-theorem among five unused leans.
- Fix: replace the table row with "m8-angle-facts, math grade 8 unit 1, days 1 to 20, taught just before,
  retrieved". Item 3: "Row change applied in eld.csv (543dba40b): g8-ma-argue now leans on m8-congruence and
  m8-angle-facts." Item 5: four leans.

### 7. Minor. 9-12 seam table lacks grade 8 unit numbers

- LAYER: process. REPEAT: yes. Confidence: high.
- What is wrong: For the lead item 7 says the 6-8 frame is still being written; it is written. The Picked-up table
  has no "Its unit" column for grade 8 (the Readiness bullet has the numbers).
- Fix: add the column (si-narrate 23, la-narrate 23, sc-explain 26, si-explain 21, ma-explain 22, sc-argue 21,
  si-argue 20, ma-argue 19, la-argue 20, la-inform 18, si-inform 18, ss-explain 24, ss-argue 25) and remove item 7.

### 8. Minor. "Grade 6 owns the cluster 6-8 ids" (3-5 Handed-on section)

- LAYER: frame. REPEAT: new. Confidence: high (the 6-8 frame and eld.csv give ownership to grade 8).
- Fix: "Grade 8 owns the cluster 6-8 ids; grades 6 and 7 carry them."

### 9. Minor. Grade 2 routine misnamed at the K-2 seam (3-5)

- LAYER: frame. REPEAT: new. Confidence: high.
- What is wrong: 3-5 calls grade 2's routine "tell, ask, retell"; the K-2 frame names it "tell, answer, retell".
- Fix: quote it as "tell, answer, retell", or say plainly that grade 3 renames it and why.

### 10. Minor. "common ancestry" handed on but not picked up (6-8 to 9-12 seam)

- LAYER: frame. REPEAT: new. Confidence: high.
- What is wrong: the 6-8 handed-on row says g8-sc-argue grows into "common ancestry and ecosystem stability"; 9-12
  unit 4 uses ecosystem stability and leaves common ancestry to a later host.
- Fix: in 6-8, "grows into ecosystem stability argued in Biology".

### 11. Minor. SI riding rule has two unnamed exceptions (6-8)

- LAYER: frame. REPEAT: new. Confidence: high.
- What is wrong: the Units bullet says SI rows ride with the unit of their shared key language use, but g6-si-inform
  rides in narrate unit 1 and g8-si-explain in argue unit 21 (reasons are in the rows). Unit 21's retrieval names
  unit 15 only.
- Fix: name the two exceptions in the bullet; add "retrieves g7-si-explain (unit 12)" to unit 21.

### 12. Minor. Language Dive named without edition; one UK spelling (6-8 base text)

- LAYER: base text. REPEAT: yes (pilot E13). Confidence: high.
- Fix: "EL Education K-5 Language Arts, 2017 edition, CC BY 4.0 (the 2025 edition is CC BY-NC and is not used)".
  "catalogue id" to "catalog id".

### 13. Minor. "'argue' is a false friend in part" (6-8 unit 20)

- LAYER: frame. REPEAT: yes (cognate wording). Confidence: high.
- Fix: "argüir and argue are cognates, but argüir is formal; argumentar or sostener is the everyday word, and
  discutir is closer to quarrel."

### 14. Minor. Host-timing lists incomplete (3-5 unit 3, 9-12 unit 20)

- LAYER: frame. REPEAT: yes (pilot E6, host timing named). Confidence: high (calendar.csv).
- What is wrong: 3-5 unit 3 runs school days 39 to 57, 9 days past its host (social studies grade 3 unit 2, school
  days 25 to 48), and is not in the "just after" list. 9-12 unit 20 (days 17 to 34) uses e11-info-structure, taught in
  ELA grade 11 unit 3 (days 35 to 55), and is in neither the "ahead" nor the "later host" list; only the cross-subject
  table explains it.
- Fix: add 3-5 unit 3 to the "just after" list; add 9-12 unit 20 to the "a few days ahead" list with "uses
  e11-info-structure ahead of ELA unit 3".

### 15. Minor. SI review uses without full ids (9-12)

- LAYER: frame. REPEAT: yes (pilot E1 form). Confidence: high.
- What is wrong: units 6, 8, 9, 10, 12, 16, 18, 21, 24 to 27, 29, 30 and 34 to 36 say "SI Argue (review, carried)"
  and similar, without the id or owner.
- Fix: "WIDA.ELD-SI.4-12.<use>, carried; owned in grade 4" in each.

### 16. Minor. Mode-less id in the newcomer strand (all three)

- LAYER: frame. REPEAT: yes (the pilot uses the same shorthand). Confidence: high.
- What is wrong: WIDA.ELD-LA.2-3.Inform, 4-5, 6-8 and 9-12 .Inform are not ids; LA ids take a mode.
- Fix: "both WIDA.ELD-LA.x.Inform ids (Interpretive and Expressive)".

### 17. Judgment call. Owner-year SC Explain carries two mechanisms in 13 days (6-8 unit 26)

- LAYER: frame. REPEAT: new. Confidence: medium.
- What is wrong: the owning unit for the 6-8 SC Explain ids teaches natural selection and force and mass in 13 days,
  and no course-level check samples the row.
- Fix: keep natural selection as the one taught mechanism, force and mass as day-2 retrieval only, and set the
  end-of-unit task on natural selection; say so in the unit row.

## Settled by the expert

| Question | Settled as | Why |
|---|---|---|
| 3-5 For the lead item 3: grade 5 gravity argument | Leave the gravity claim to science; g5-sc-argue is met on plant matter in unit 19, and the fixer notes that in the row | The ids ask for argument from evidence, not a topic; plant matter is the host's own content |
| Cognate wordings (findings 4, 13) | As written in those fixes | Etymology and register, not false friends |
| 9-12 picked-up unit numbers (finding 7) | The list in finding 7 | Taken from the 6-8 Units table |
| 9-12 SI shorthand | Full id, "owned in grade 4" | Matches the pilot's E1 form |

## Calendar clashes among after-core courses (for the lead calendar pass; not findings)

- Grade 3 week 27: theater.
- Grade 4 week 15: music, SEL. Week 29: health, library.
- Grade 5 week 18: dance, media arts, PE, theater, visual arts. Week 28: health, library.
- Grades 6 and 7 week 17: dance, health, media arts, PE, theater, visual arts. Grade 7 week 18: library.
- Grade 12 week 16: PE.
- Week 32 in grades 6 to 12: many courses (finals week, allowed).
- The 3-5 For the lead item 5 misses grade 4 week 15 and grade 5 week 18. Grade 8's mid-year check (days 98 and 99,
  week 20) shares week 20 with civics days 96 and 97, which CALENDAR.md rule 3 allows (no shared day).

## What is right and should not be touched

- One host per unit, cited by course days, with "If later" lines; hosts taught later are marked "not used".
- SI in every unit, with recurrence maps in the spine bullets.
- Entry points change the help, never the task.
- Days follow the host window first; tight units named; rows no check samples are named.
- Checks off core check weeks in grades 3 to 5; grades 6 to 12 year-end in finals week 32.
- 9-12 handles grade 12 electives, the senior calendar and the 18-or-over rule.
- The 543dba40b row changes are in eld.csv (fuerza, cuadrado, capítulo, razón, ejemplo, señal; g8-ma-argue on
  m8-congruence and m8-angle-facts).
- Host texts exist in the host ELA frames (The Cask of Amontillado, The Postmaster, An Occurrence at Owl Creek
  Bridge, Self-Reliance, Civil Disobedience, Two Views of the Mississippi).
- Paper path, no student data, and safety are handled.

## Could not judge

- Whether each owned unit teaches every part of its WIDA expectation: the printed framework lists were not opened
  (downloading needs permission), and I did not rely on memory for them.

## For Cory

- Newcomer strand delivery (people and time), already raised in the pilot; nothing new.

## Sources

- The repo files listed under What was read.
- WIDA ELD Standards Framework 2020 (URL in finding 2): named, not opened.
- incertidumbre and uncertainty from Latin certus; argüir from Latin arguere: from memory, standard etymology.

## For the source list

- WIDA ELD Standards Framework 2020 PDF, free from wida.wisc.edu: the printed expectation pages per cluster should
  be the reference for every owned-id check.

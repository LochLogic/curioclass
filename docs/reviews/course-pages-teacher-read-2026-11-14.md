# Course pages: a teacher read and the file limit (2026-11-14)

Later row L19 (Cory approved 2026-11-14). Two parts: a read of the hidden course and unit pages as a classroom teacher
and a parent teaching at home, with fixes at source; and where the site's files go against the host's file limit. The
credits line (L21) was left alone. Pages stay hidden (`SHOWN = False`). No git, no deploy, no frame edited.

## Part 1: the teacher read

### Pages read

Built with `scripts/course_pages.py build` into a scratch copy of a full build, read as page text and in a local preview.
About 70 pages: the course page and at least two unit pages for one course per subject in each band, plus the units
with the most dropped sentences.

| Band | Course page and units read |
|---|---|
| K-2 | ELA 1 (course, U1, U3); Math K (course, U1, U4, U8); Math 1 (course, U6, U7); Math 2 (course, U5, U6, U8); Science 2 (course, U1, U2, U4); Social Studies 1 (course, U1, U3, U5) |
| 3-5 | ELA 3 (course, U1, U2, U3); Math 4 (course, U1, U5, U9); Science 4 (course, U1, U3, U5); Social Studies 5 (course, U1, U4, U8) |
| 6-8 | ELA 7 (course, U1, U3, U6); Math 6 (course, U1, U4); Science 8 (course, U1, U2, U4); World Geography and Ancient Civilizations I (course, U1, U4, U8) |
| 9-12 | ELA 10 (course, U4, U6); ELA 11 (course, U1, U5, U6); Algebra II (course, U1, U4, U7); Biology (course, U1, U5); US Government and Politics (course, U1, U3, U9) |
| Most dropped | Science 8 U1 (6), Science 7 U1 (6), ELA 3 U2 (6), Science 8 U2, Science 7 U2, U4, U5, Science 6 U3, U4, U6, Physics U7, U8 (5 each) |

Preview: Math 6 U4, Science 2 U2, ELA 10 and US Government U3 at phone width (375 px) and in the desktop pane. No
sideways scroll at either width; the Standards list, its new note and the check timeline wrap cleanly.

### What was wrong, and the fix (all in `scripts/course_pages.py` and `site/templates/courses/`)

1. **Brand names caught ordinary words.** The names filter was case-blind, so "OSPI" dropped sentences with
   "hospital", "Khan" dropped Genghis Khan, "Amazon" dropped the river, "Canva" dropped "canvas", "Flipgrid" "flip".
   Names now match case-sensitive at word edges.
2. **Planning words caught ordinary words.** "production" and "reproduction" (BASELINE/PRODUCTION), "probe into",
   "edge guard", "National Guard", "resource availability", "a frame-by-frame look", "rows and columns", "logarithm
   with base 2", "retaught in brief". Each pattern narrowed so the real planning sense is still dropped.
3. **Planning language that got through.** Added: "Candidate" (capital), idle grades, base days, "the brief",
   "stitch", day transfers, ISO dates, the "sources/values/stagger rule" names, thread numbers, "rule b", day budget,
   "Also met", "Lettered parts", "the progression", "(+)", "settled by", "expert read", "of our own", "densest",
   "by codes", Oak unit names, "IM 3", "Supporting cluster", "Standards in full".
4. **Rewordings instead of drops** (TIDY list): science K-5 "clarification" asides removed; "No-kit path:" reads
   "Without a lab kit:"; "Stand-ins:" reads "Everyday substitutes:"; "Simulation listed:" reads "A simulation:";
   "paper path" reads "On paper"; "the band" reads "the grade band"; "measure target about 600" reads "reading level
   about 600"; "Boundary:" reads "Limits:"; "Retrieval task on" reads "A short look back at"; "One added lesson" reads
   "One lesson"; base lesson numbers such as (6.11) removed.
5. **Safety notes were being lost.** Science 7 U1 dropped the whole sentence naming the teacher-only demonstrations
   (flame tests, peroxide, heating water, splitting water) and their protocol, because it began "The base's";
   Science 8 U1 and U2 dropped the laser handling sentence ("the safety agent's read"). Now the lesson numbers and
   "the base's" are removed and the safety text stays; the laser line reads "unless the teacher sets up a controlled
   apparatus".
6. **Standards codes in prose.** A code used as a sentence label ("RL.9-10.2: ...", "6.RP.A.3 is begun here:") is now
   stripped, and a parenthetical clause that only cites codes is dropped (the Standards list already shows them).
   Codes are matched whole (the old match cut "RST.9-10" out of "RST.9-10.3" and left "Also met (literacy).3").
7. **Unreadable codes.** Each unit's Standards list now carries one plain note on how to read a code for that subject
   (`CODE_HELP` in course_pages.py, shown as `.cp-note` under the list in unit.html), without naming any standards
   document.
8. **Sentences cut mid-thought.** Clauses are split on ";" only outside parentheses (the old split cut "(two
   friends...; a child who plays her own way)"); a kept clause is capitalised; a sentence ending in ")" gets its period.
9. **Timers.** HS ELA "a timed paragraph/essay", "timed analytic writing", "once timed" now read "written in one
   sitting (no timer shown)". Every remaining "timed" on the 450 pages says "no timer", "never timed" or "untimed",
   except one (Science 4 U6, below).
10. **Check labels** like "Check 1 (day 80; respond day 81)" and "Course-level check 2, year-end course-level check"
    now read "Check 1" and "Course-level check 2, year-end" (the days already show beside the label).

Rendered scan of all 450 pages after the fixes: 0 em dashes, 0 "Curio" alone, 0 company or document names, all 450
carry noindex. Tone: no talking down found; notes read as one teacher to another.

### Frame wording to change (not edited; for the frame owners)

The filter can only drop or reword by pattern. These need the frame text itself.

| Frame | Line | Now | Proposed |
|---|---|---|---|
| science-grade-4 | 160 (U6) | "timed in early and late rounds" | "counted in early and late rounds" |
| english-language-arts-grade-3 | 158 to 161 (U1 to U4) | "The unit's word list" (a fragment, filter drops it) | "The unit's word list, studied and spelled." |
| english-language-arts-grade-1 | 132 (U3) | "(r-controlled vowels stay in grade 1, the stitch decision)" | "(r-controlled vowels are taught in grade 1)" |
| english-language-arts-grade-11 | 13 | "Anchors sit in the 11-CCR band (... the standard's grade 11 line)" | "Anchors sit at the high end of the grades 11 to 12 range" |
| english-language-arts-grade-11 | 122 (U1) | "Mather as the RI band text" | "Mather as the informational text" |
| english-language-arts-grade-12 | 120 (U6) | "the course's balance rule" | "keeping the year's texts balanced" |
| english-language-arts-grade-10 | 137, 138 (U6, U7) | "the facts and backed sources rule"; "(see Cross-subject)" | "every claim backed by a named source"; delete the aside |
| english-language-arts-grade-9 | 139 (U7) | "(see Cross-subject)" | delete |
| english-language-arts-grade-7 | 146 (U1) | "It starts thread 2" | "It starts the year's second strand, ..." (say the strand) |
| english-language-arts-grade-2 | 127 (U2) | "Product names in L.2.2a are invented, never real brands." | "Product names in the capital-letters practice are invented, never real brands." |
| math-grade-4 | 151 (U6) | "the decimals rule" | say the rule itself ("decimals are written to tenths and hundredths only") |
| math-grade-6 | 134 to 136 (U2 to U4) | "6.RP.A.3 is begun here", "Finishes 6.RP.A.3", "Opens with a readiness check on 5.NF.B.7" | "Begins ratio and rate reasoning", "Finishes ratio and rate reasoning", "Opens with a readiness check on dividing unit fractions" |
| algebra-i | 141, 142 (U3, U4) | "... finished in Algebra II" (with code) | "fitting functions to data, finished in Algebra II" |
| math-grade-1 | 142 (U8) | "so ELA's year-end check holds week 32 alone" | delete (scheduling between courses) |
| science-kindergarten | 118 (U3) | "Then K-PS2-2:" | "Then students judge whether a push did what they planned:" |
| science-grade-3 | 136, 137 (U1, U2) | "(see Cross-subject)" | delete |
| world-geography-and-ancient-civilizations-i | 134, 137 (U1, U4) | "The anchor opens with 6.T1 and 6.T2", "objective 2's worked case", "the anchor's order" | "The year opens with how we study the past and with geography", "the worked case", "in the usual order" |
| civics-government-and-civic-life, economics, world-geography-and-ancient-civilizations-ii | 199; 8; 33 | "the anchor's order" | "the usual order" |
| us-government-and-politics | 143 (U9) | "proposes a day transfer" | delete (planning) |
| HS ELA frames (9 to 12) | unit rows | inline codes in prose ("adding SL.11-12.1a to d (...)", "W.11-12.2a to f", "RL.9-10.10 at the high end") | keep codes only in the Owned standards column; say the skill in words in prose |

General rule for frame writers that would end most drops: write "What students learn", "Why" and teacher notes as
if a teacher will read them; keep base lesson numbers, agent reads, the "base" and codes in their own columns.
58 bare codes remain in prose across the 397 units, mostly HS ELA and math.

## Part 2: the file limit

### The host's limit

Cloudflare Workers static assets: "Files per Worker version: 20,000 (Free), 100,000 (Paid)"; 25 MiB per file.
Workers Free allows 100,000 Worker requests a day; requests to static assets are free and unlimited, but a path in
`run_worker_first` always runs the Worker and counts, and on Free answers 429 past the daily limit.
Sources: https://developers.cloudflare.com/workers/platform/limits/ and
https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/ (read 2026-11-14).

### Where the files go

A full build with `--library --closet --courses`:

| Folder | Files | Kind |
|---|---|---|
| library | 8,401 | 6,603 jpg (served from R2), 1,797 html |
| topics | 6,319 | 3,848 webp (served from R2), 1,634 html, 762 csv, 75 svg |
| standards | 1,662 | html |
| closet | 1,178 | 919 html, 205 json, 54 svg |
| tools | 1,125 | 1,042 html, 83 svg |
| courses | 450 | html (hidden, in .assetsignore) |
| assets, collections, styles, grades, recess, subjects, other | 341 | js, mp3, svg, fonts, html |
| **Total on disk** | **19,476** | |

The 19,468 in docs/reviews/site-course-pages-2026-11-14.md counts every file on disk. The deploy does not upload the
10,451 pictures that `.assetsignore` lists (they are served from R2 by worker/index.js). **What counts against the
limit today is about 8,574 files, or 9,024 with the course pages shown**: 45 percent of 20,000, not 97 percent.

### What the plan adds

52 courses, 397 units, about 160 days each:

| Layout | Day pages | Section pages | Uploaded total | Against 20,000 |
|---|---|---|---|---|
| Today, course pages shown | 0 | 0 | 9,024 | 45% |
| One file per day, 52 courses (sections about 4 a unit) | 8,320 | about 1,600 | about 18,950 | 95% |
| Same, plus a printable and an At home page per day as files | 24,960 | about 1,600 | about 35,600 | over |
| One file per day, all 105 planned courses | about 16,800 | about 3,200 | about 30,000 | over |
| One page per section, days as anchors, 52 courses | 0 | about 1,600 | about 10,600 | 53% |
| One page per section, days as anchors, 105 courses | 0 | about 3,200 | about 13,000 | 65% |

### Options

1. **One page per section, each day an anchor on it** (/courses/x/unit-3/section-2/#day-4). Biggest saving: about
   8,300 files for 52 courses, 16,800 for 105. A section of about 4 days is one read for a teacher; the At home view
   becomes a toggle on the same page and the printable one PDF per section, not per day.
2. **Bundle the small data files**: topic word CSVs (762) into one file per subject, closet JSON (205) the same.
   About 950 files saved. Cheap, but small next to option 1.
3. **Serve day pages from R2 through the Worker**, as the pictures are now. No file limit, but every day view is a
   Worker request: on Free, 100,000 a day, then 429 errors. Fine for pictures, risky for the pages people read.
4. **Workers Paid plan**: the limit is 100,000 files. Room for one file per day at 105 courses, with a monthly fee.
5. **A second site for courses** (its own Worker and 20,000 files, on a subdomain or route). Works on Free but
   splits the build, search and links.

**Recommendation.** The real count is about 9,000 uploaded files, so there is room now; build sections as one page
each with days as anchors (and At home and printables inside that page), which keeps all 105 courses near 13,000.
Keep the Paid plan as the fallback if day pages must be separate files, and bundle the CSV and JSON data only if
room gets tight.

## Check results

- `python -X utf8 scripts/course_pages.py check`: exit 0. 52 courses, 397 units, 450 pages. Kept and dropped by
  column: What it checks 253/7; What students learn 1,173/143; Why this unit, here 781/238; anchor 169/1; teacher
  notes 1,025/347 (before this read: 255/5, 1,254/69, 828/191, 169/1, 1,041/334). Most new "learn" drops are
  standards bookkeeping ("Also met ...", "Lettered parts ...") and skill-id review lines.
- `python -X utf8 scripts/plan.py check`: exit 0, 0 frame failures (notes only).
- A full build with `--closet` still stops on the closet Word Wall (social-studies.txt line 30, "culture" definition
  13 words against a cap of 12); not part of this work, so the read used a build without `--closet` plus an earlier
  full build for the file count.

## Files changed

- scripts/course_pages.py: NAMES, PRIVATE, CODE, TIDY, TIMED; new top_split, no_codes, cap and CODE_HELP; check
  labels. SHOWN still False.
- site/templates/courses/unit.html: the code note under the Standards list.
- site/templates/courses/_style.html: `.cp-note`.

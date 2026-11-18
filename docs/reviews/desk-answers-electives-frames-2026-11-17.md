# Desk answers applied: the six core elective frames, 2026-11-17

Cory answered ten calls on Desk card q-electives-frames-1 on 2026-11-17. This records how each was applied. Decision
log line: docs/agents/decisions/DESK-ANSWERS.md, 2026-11-17.

## 1. Grade 12 math route

Precalculus, then Calculus, on the accelerated path (L15); Precalculus the stated prerequisite; straight from Algebra II
a named alternative with a bridge of about 20 lessons.
- docs/courses/precalculus/frame.md: header grade line, Who takes it bullet, For the lead 1 settled.
- docs/courses/calculus/frame.md: header ("Precalculus is the stated prerequisite"), route bullet (the scope writer
  counts on the accelerated path), alternative bullet (stays named), For the lead 1 and 8 settled.
- data/courses.csv: calculus notes now "first-year college level, both semesters' content; prerequisite: Precalculus"
  (the course page reads its notes from here).
- data/plans/later.csv L15: note added (the path is also the route to Precalculus in grade 11, Calculus in grade 12);
  L15 stays open, since it still needs its compression plan.

## 2. High school math focus (L49)

- docs/RUBRIC-MATH-HS.md: the intro line now points to a new section, "The grade 12 courses: Precalculus, Statistics
  and Calculus": the owned-outcome account in place of 1a to 1c, one cap of 15 percent of unit minutes for review and
  readiness (what counts and what does not, stated once), the modeling cycle kept whole.
- The three math frames' Focus bullets now cite that section instead of "the shared answer"; their For the lead items
  on L49 and the cap are settled (Precalculus 2 and 7, Statistics 1 and 9, Calculus 7).
- data/plans/later.csv L49: done.

## 3. Earth and Space Science grade

Typical grade 12, open to grades 10 to 12 for a student who has finished, or is taking alongside, Biology, Chemistry
and Physics.
- data/courses.csv: `earth-space,science,Earth and Space Science,10-12,12,n,"Follows Biology, Chemistry and Physics"`.
- docs/courses/earth-and-space-science/frame.md: header grade line; For the lead 1 settled, with the one design line
  this opens: a student taking Physics alongside (units 1 to 3 come before Physics unit 9) or not yet past Algebra II
  (units 8 and 9) gets a printed catch-up pack and parallel support inside the retrieval task, no added day.
- frame.py sync run (frames.csv and the calendar unchanged in count: 58 courses, 782 calendar rows).

## 4. Base texts

Downloaded on 2026-11-17 into S:\CurioClass-sources, each in its own folder with NOTES.md (what it is, licence as read
at source, rules), MANIFEST.csv (file, url, date, bytes, sha256, licence, version) and licence/ (saved pages). The store
README and docs/sources/BASE-TEXTS.md (Base texts table, Our own list, Credit lines) record them. All from the
publisher or the author's own site.

| Folder | What | Files, size | Licence, as read at source |
|---|---|---|---|
| openstax-precalculus-1e | OpenStax Precalculus 1st edition, Precalculus-OP_9wwF7YT.pdf (revision PR-2015-002(03/17)) | 1 PDF, 86.2 MB, plus book record | CC BY 4.0 (copyright page; publisher's book record: retired, CC BY 4.0) |
| openstax-statistics | OpenStax Statistics 2020, high-school-statistics_-_WEB.pdf | 1 PDF, 31.5 MB | CC BY 4.0 (copyright page; book record: live) |
| openstax-introductory-statistics-1e | OpenStax Introductory Statistics 1st edition, IntroductoryStatistics-OP_i6tAI7e.pdf | 1 PDF, 26.6 MB | CC BY 4.0 (copyright page; book record: retired). 2nd edition is CC BY-NC-SA: never |
| lane-online-statistics | Online Statistics Education (Lane), Online_Statistics_Education.pdf | 1 PDF, 34.1 MB, plus 2 site pages | public domain (site home page) |
| contemporary-calculus | Hoffman, Contemporary Calculus: archive-2016\ (Calculus_all.html and 152 PDFs) and the current site's 101 PDFs | 257 files, about 349 MB | archive page: CC BY 3.0 US. Current site: no statement on the home page; the 2020 combined volume for chapters 4 to 8 says CC BY-SA 3.0 US |
| physical-geology-2e | Earle, Physical Geology 2nd Edition, PDF and EPUB | 2 files, 464.8 MB, plus exceptions page | CC BY 4.0 except where noted; the book's exceptions page saved (those figures never reused) |
| openstax-astronomy-1e | OpenStax Astronomy 1st edition, Astronomy-OP_zItt6LJ.pdf | 1 PDF, 161.2 MB | CC BY 4.0 (copyright page; book record: retired). Astronomy 2e is CC BY-NC-SA |
| noaa-jetstream | NOAA NWS JetStream, 134 lesson pages as HTML (no images) | 136 files, 15.9 MB | public domain unless noted (Weather Service disclaimer page): no endorsement implied, not presented as official material; images credited to others excluded |
| harris-environmental-sciences-2023 | Harris, Introduction to Environmental Sciences and Sustainability (UWF 2023), PDF and EPUB | 2 files, 95.0 MB | CC BY 4.0 except where otherwise noted (copyright page); built from Fisher's Environmental Biology (CC BY) |

Frames: every Pending base-text marker is rewritten to say what is now true (Precalculus, Statistics, Calculus, Earth
and Space Science, Environmental Science), and For the lead items on loading are marked done.

Notes:
- **Contemporary Calculus licence conflict (for Cory).** The Calculus frame said CC BY 3.0 US from the current site.
  The current site's home page states no licence, and its 2020 combined volume says CC BY-SA 3.0 US. Only the author's
  archive page (2016) says CC BY 3.0 US. Applied: the archive copy is the base and the newer PDFs are reference only;
  frame Base text bullet, BASE-TEXTS.md and NOTES.md say so. The archive's section numbering may differ from the Source
  map, which the scope writer checks. If Cory wants the newer text, share-alike would bind adapted days.
- **Statistics.** Cory named Introductory Statistics; the frame's Source map is built on OpenStax Statistics (2020),
  which is drawn from it. Both are loaded; the frame keeps Statistics 2020 first and names Introductory Statistics as a
  second base with its own credit line.
- **Precalculus.** The publisher's PDF is the 2017 printing; the frame's map was built from the web edition's 2021
  archive version. The scope writer checks section numbers against the PDF.
- Not downloaded: Fisher's Environmental Biology (the Environmental Science fallback) and Webb's Introduction to
  Oceanography (optional for Earth and Space Science unit 6); neither was on Cory's list. No download failed.

## 5. Environmental Science unit 5

- docs/courses/environmental-science/frame.md: the Sensitivity reads bullet now says the released-material, no-contact
  condition is Cory's and that a fresh sensitivity agent reads unit 5 before its unit plan is written; For the lead 2
  settled.
- data/plans/later.csv L68 (new): the fresh read, triggered before the unit 5 plan is written.

## 6. Cost ceilings (a year, class of 30)

- Precalculus and Calculus about $400; Statistics $450: a Cost ceiling bullet in each frame's brief (printing within it,
  reusables bought once), For the lead cost items settled (the senior-calendar half of each stays open). No math unit
  passes $150.
- Earth and Space Science and Environmental Science $1,000 each, reusable kit shared: the sentence in each "Unit by
  unit" section intro, For the lead 10 and 11 settled. Units over $150 got a cheaper route in their cost cell (item-level
  choices): Earth and Space Science unit 1 (about $480, cheaper route about $250: shared mineral sets, 5 compasses,
  borrowed eye protection); Environmental Science unit 1 ($195 to about $105), unit 3 ($200 to about $90), unit 4 ($160
  to about $80).

## 7. Same-grade seams

Kept in prose by course order. Earth and Space Science For the lead 4, Environmental Science 4 and Psychology 2 settled;
Calculus For the lead 1 points to the row. data/plans/later.csv L67 (new): the gate change, triggered when a scope needs
it.

## 8. Widened science outcomes

No change to outcomes or days. Earth and Space Science For the lead 3 and Environmental Science For the lead 3 marked
settled, kept.

## 9. Calculus extensions

docs/courses/calculus/frame.md: new brief bullet "Extensions stay extensions": every named extension listed, never an
outcome, and the first cut on the accelerated route, before any step of A tight course's trim order. For the lead 2
settled. Reading of "power series and similar": calc-power-series (CUR-CA.30, unit 11) is an owned outcome in this
frame, so it stays owned; the further series topics the frame already marks as extensions (the binomial series for
powers that are not whole numbers, products of series, e to the i theta) are the ones listed. If Cory meant CUR-CA.30
itself, that is a scope change for him (it would drop an owned outcome and free 7 days).

## 10. Psychology unit 15 and the Statistics lens

- docs/courses/psychology/frame.md: For the lead 1 settled: unit 15 is required.
- docs/agents/lenses/statistics.md (new): the data-teaching lens, the GAISE College Report (2016) and Pre-K-12 Report II
  (2020) recommendations in our own words, no copied text, no endorsement claim; checks for the investigative cycle,
  variability and context, concepts before recipes, active learning and technology, assessment, data privacy.
  docs/agents/lenses/math.md points Statistics reads to it; RUBRIC-MATH-HS.md names it.
- docs/courses/statistics/frame.md: Focus bullet references the lens; For the lead 1 settled.

## Gates

- `python -X utf8 scripts/frame.py check` on the six frames: 0 failures each (all 58 frames: 0 failures).
- `python -X utf8 scripts/stale.py check`: 62 files, 0 failures.
- `python -X utf8 scripts/frame.py sync`: 58 courses, 782 calendar rows.
- `python -X utf8 scripts/plan.py check`: exit 0, 0 catalogue failures.

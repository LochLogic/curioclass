# Build errors L20: worksheet rows (2026-11-14)

Task: data/plans/later.csv row L20. The whole-site build (`scripts/build_site.py`, without `--closet`) stopped on
worksheet data errors. All fixed in the data; one build gating line fixed so `check_site.py` passes. Nothing deployed.

## Where the data lives

- Built sheets: `data/closet/worksheets/<unit>.md`, one file per class, each sheet headed `# <n>. <title>`.
- Concept lists (the rule the build checks against): `docs/worksheets/social-studies.md`, one `## <unit>: ...`
  section per class, rows `| n | title | type | topic | does |`.
- The rule (`scripts/worksheets.py`, `load()`): every built sheet's number must exist in its class's concept list,
  and its title must match that row's title exactly. The sheet's topic, and so its standards, come from that row.

## Cause

The social studies course redraw on 2026-11-13 (P1b) moved concept rows to new classes and renumbered them in
`docs/worksheets/social-studies.md`, but the built sheets in `data/closet/worksheets/` stayed under their old class
and number. The eight errors in L20 were only the first failure in each file: `load()` stops at the first bad sheet,
so the real count was **27 stale sheets** across the same eight files. Every one of the 27 titles exists exactly once
in the social studies concept lists (one title, State History Timeline, also appears in eld-4, which is a different
sheet and was ignored), with the same topic as before, so each sheet's content and standards carry over unchanged.

## Fix: each sheet moved to the class and number its concept row now has

Content copied byte for byte; only the `# n.` heading number changed (non-blank line count 2228 before and after).
Files kept in number order. Two new class files created: `us-hist-1.md` and `world-hist-2.md`. No other file
referenced any of these sheet numbers (checked generated.csv and data/; no target slot was already used by a written
or generated sheet).

| Before (file #n) | After (file #n) | Title | Topic (unchanged) |
|---|---|---|---|
| ss-2 #5 | ss-1 #43 | Who Leads Our Town? | Community Helpers and Government |
| ss-2 #38 | ss-1 #48 | Changemaker Timeline | Heroes and Changemakers |
| ss-4 #6 | ss-3 #41 | State History Timeline | State History |
| ss-4 #24 | ss-3 #47 | Local, State or Federal? | State Government |
| ss-4 #29 | ss-3 #51 | What We Sell, What We Buy | State Economy and Resources |
| ss-5 #6 | ss-4 #48 | Environment Shapes Life | Indigenous Peoples of North America |
| us-hist-8 #1 | us-hist-1 #1 | After the French and Indian War | Road to Revolution |
| us-hist-8 #31 | us-hist-1 #13 | What to the Slave Is the Fourth of July? | Slavery and Sectionalism |
| us-hist-8 #32 | us-hist-1 #14 | Harriet Jacobs in Her Own Words | Slavery and Sectionalism |
| us-hist-8 #44 | us-hist-1 #20 | Three Amendments, Three Promises | Reconstruction |
| us-hist-hs #1 | us-hist-1 #23 | Carnegie's Gospel of Wealth | Industrialization and the Gilded Age |
| us-hist-hs #6 | us-hist-hs #1 | Who Is Missing From This Archive? | Missing Voices Archive |
| us-hist-hs #17 | us-hist-hs #3 | Harlem Renaissance Voices | Roaring Twenties and the Great Depression |
| us-hist-hs #24 | us-hist-hs #9 | Mobilizing the Home Front | World War II and the Home Front |
| us-hist-hs #29 | us-hist-hs #13 | Brown v. Board and Mendez | Civil Rights Movement |
| us-hist-hs #40 | us-hist-hs #22 | Trace the Documentary's Sources | Behind the Documentary |
| world-geo-6 #25 | world-hist-7 #54 | Greek City-States Map | Ancient Greece |
| world-geo-6 #30 | world-hist-7 #57 | Roman Republic Government | Ancient Rome |
| world-hist-7 #6 | world-hist-hs #10 | Procopius on Justinian and Theodora | Fall of Rome and the Byzantine Empire |
| world-hist-7 #25 | world-hist-hs #16 | Black Death Spread Map | Medieval Europe |
| world-hist-7 #31 | world-geo-6 #52 | Maya, Aztec, Inca Map | Civilizations of the Americas |
| world-hist-7 #43 | world-hist-hs #21 | Zheng He and Columbus Compare | Age of Exploration |
| world-hist-hs #1 | world-hist-2 #1 | From Copernicus to Newton | Revolutions and Enlightenment |
| world-hist-hs #18 | world-hist-2 #10 | MAIN Causes of War | World War I |
| world-hist-hs #25 | world-hist-2 #15 | The Great Depression Worldwide | Between the Wars |
| world-hist-hs #30 | world-hist-2 #19 | Wartime Deaths Data | World War II and the Holocaust |
| world-hist-hs #42 | world-hist-2 #26 | Winners and Losers of Globalization | Globalization Today |

Originals of the ten touched files (ss-1 to ss-5, us-hist-8, us-hist-hs, world-geo-6, world-hist-7, world-hist-hs)
are kept in `S:\CurioClass-archive\worksheets-before-l20-2026-11-14\`.

### Follow-on fix: Grade 1 passage length (ss-1 #43, Who Leads Our Town?)

Moving the sheet from Grade 2 to Grade 1 tripped the passage rule ("passage of 98 words, want 40-90 for this
grade"). Trimmed to 90 words (my item-level call), keeping every fact the five questions and the stretch test:

- Before: "They meet each month to make town laws and to decide how to spend the town's money."
  After: "They meet each month to make town laws and plan how to spend money."
- Before: "The council talked about it and voted yes." After: "The council voted yes."
- Before: "Chief Sam Lee leads the town's police officers." After: "Chief Sam Lee leads the police officers."

## Build fix: research card links on topic pages (`scripts/build_site.py`, topic page loop)

With the worksheet errors gone the build ran to the end for the first time, and `check_site.py` then failed with
64 broken links to `/closet/research-cards/...` on 20 topic pages. A build without `--closet` deletes `dist/closet/`,
and every other Supply Closet item on the topic page render (worksheets, generator links, Word Wall, games, charts) is
already gated on `CLOSET_LIVE`; research cards were not. Not a checker problem and not data: the page linked to
pages the same build removes. Added one line after the `rcards = ...` line:

    rcards = rcards if CLOSET_LIVE else []  # research cards live in the Supply Closet, so no links while it is held back

With `--closet` the section shows as before.

## Results

- `CURIO_DIST=<scratch> python -X utf8 scripts/build_site.py`: passes, 4709 pages, 83 built tools, 717 on the bench,
  381 in sitemap (built into a scratch folder, not dist/, since dist/ is the folder wrangler.jsonc deploys).
- `CURIO_DIST=<scratch> python -X utf8 scripts/check_site.py`: passes, 3470 pages checked, 0 broken internal links,
  0 external loads.
- `python -X utf8 scripts/plan.py check`: passes, 52 courses, 0 catalogue failures.
- `build_site.py --closet` (scratch): worksheets pass; it stops only on the Word Wall definition
  `social-studies.txt:30 culture` (13 words, cap 12), left untouched for Cory.

## Notes for the lead

- `dist/` was cleared by mistake: I ran `build_site.py --help` to read its options, but the script has no option
  parser, so it ran a real build into `dist/`, which deletes `dist/` before validating and then stopped on the
  worksheet errors. `dist/` now holds a partial build. It is gitignored and any build refills it, but it is the folder
  wrangler deploys, so rebuild before any deploy (as the deploy flow should do anyway).
- Some moved sheets changed grade (for example Grade 2 to Grade 1, grade 7 to high school World History I). The
  redraw placed the concept rows there; apart from the Grade 1 passage rule, no build rule flagged a level mismatch,
  and I did not rewrite content for level.

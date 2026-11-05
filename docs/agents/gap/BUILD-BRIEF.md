# Brief: build one new Worksheet Generator for Curio Class

Curio Class (S:\CurioClass, a free K-12 teaching site; always write "Curio Class", never "Curio" alone) has 16
Worksheet Generators: pages that make a fresh printable worksheet with an answer key from a few settings. Each is one
file, site/assets/gen/<id>.js, sharing site/assets/gen/engine.js. A review of 7,856 planned but unwritten worksheet
rows found which kinds of sheet a generator could make; your generator is one of the 10 picked to close the biggest
gaps (docs/agents/WORKSHEET-GAPS.md has the whole picture).

## Read first

1. site/assets/gen/engine.js: Gen.add(id, def), fields (select, check, number, text; `options: v => ...` and
   `show: v => ...` for dependent fields), make(v, r, d) with the seeded rng r, verify, css, the H html helpers
   (Gen.h: part, example, fill, blank, key, esc ...) and Gen.m math helpers. Do NOT edit engine.js; if you truly
   need an engine change, say so in your reply instead.
2. A reference generator close to yours: number-ops.js (practice items with a key), coordinate-plane.js (SVG drawing
   with key marks in red, class ws-ans, hidden on the student copy), organizer.js and writing-frame.js (frames for any
   typed topic), planner-log.js (logs), vocabulary.js (word banks).
3. docs/agents/GEN-OPTIONS.md: every existing generator's settings, so yours follows the same naming.
4. Your target rows: the CSV path in your prompt. Each row is a planned worksheet (unit, row number, title, type,
   module, and the Students line saying what students do). Design your settings so the generator makes as many of
   these sheets as possible WELL: a teacher who opens the row's link should feel the promise in the Students line was
   kept. You will not fit every row; fit the common patterns, skip the oddballs. A row that needs a passage, named work
   or real data stays with writers.

## Rules

1. Write only site/assets/gen/<your id>.js (and, if you need a word or fact bank too big to sit in the file, a
   second file site/assets/gen/<your id>-data.js loaded before it; say so in your reply). Do not edit engine.js,
   data/closet/generators.json, scripts/*, other generators, or anything else. Do not build, commit or deploy.
2. Fields: short lowercase ids, letters and digits only. Use `grade` for a grade field with values 'k', '1' ... '12'
   (or `band` with 'k2', '35', '68', '912' when the generator works by band, as organizer.js does), `count` for
   length (select of s/m/l or numbers, like the others), `topic` for a typed title. Every option has a clear
   teacher-facing label. Pick defaults that make a good sheet with no changes.
3. Every answer on the key is right. Write verify() so it re-works every item independently (a different computation
   than make() used, where possible). Frames and rubrics with nothing to answer use noKey like organizer.js does, or a
   key that shows a model or sample, whichever existing frame generators do.
4. Pages: a kindergarten sheet fits 1 printed page, every other grade 2 pages, student copy, at the longest count.
   Keep item counts like the existing generators' for that grade. The print check runs later (it needs a site build),
   so stay comfortably inside: assume about 22 short lines per page plus the header, and drawings take real space.
5. No em dashes anywhere (the checker fails on them). Text a child reads at sight is short and plain, with common
   names. Spanish and French text uses correct accents. Nothing that teaches a wrong fact.
6. Text fields are capped at 240 characters by the engine. A custom-data text field needs its format in the label
   (for example "Words, comma separated: run, jump, swim") and a forgiving parser that falls back to built-in data
   when the text does not parse. The checker feeds every text field `Plants & "animals" <of> the desert`, so the
   parser must survive that and still make a valid sheet. Always escape typed text with esc().
7. Comment the top of the file the way the existing ones are: what it makes, grades, skills, and standards codes where
   they apply (CCSS math and ELA, ACTFL for languages, NCAS for the arts, CSTA for computer science, Jump$tart or
   NGSS where they fit).
8. Test: from S:\CurioClass run `node scripts/check_generators.mjs <your id>` until it ends ok (it is already
   registered in data/closet/generators.json with a DRAFT blurb). The checker tries every option alone plus random
   mixes, many sheet codes each, and checks repeats, determinism, undefined/NaN, em dashes, blanks with answers, and
   your verify(). For a visual check you may render a sheet to HTML with a small node script in your own temp folder
   (load engine.js and your file into a vm context like the checker does, then Gen.render), but do not leave files in
   the repo.
9. Quality over saved work. A mode that cannot be done well is better left out, and say so.

## Reply (short)

- The fields: id, values, what each does.
- A one-sentence blurb for the generator list, in the style of data/closet/generators.json, and its grade span.
- Which target rows it now makes well, as a CSV block with header `unit,n,query,note` (query = the settings as a
  query string, for example `grade=3&skill=ten&count=m`; note = 3 to 10 words). Be strict: only rows whose Students
  line the sheet really keeps. Then a one-line count of rows fit and rows left, and the main reasons rows were left.
- Anything you left out and why, and anything you think needs Cory's eye (a content choice, a standard).
- The checker's final line.

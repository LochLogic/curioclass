# Supply Closet: teacher resources (plan)

Status: concepts AGREED by Cory 2026-10-26 (decisions at the bottom). This file is the implementation plan; nothing
is built yet. Open questions for Cory are marked **Q**.

The Supply Closet is the teacher-resources side of Curio Class: things to print and put up that go with the tools.
It is organized like a real supply closet, as shelves:

| Shelf | What | Keyed to | Phase |
|---|---|---|---|
| **Sub Day** | A print-ready packet for a substitute, one per tool | tool | B |
| **Word Wall** | Vocabulary cards and a student glossary | module | C |
| **Posters and Anchor Charts** | Anchor chart per module (finished and fill-in), a small set of year-long posters per band | module / band | D |
| **Family Game Night** | Low-materials games to play at home, 2-3 per subject per grade | grade + subject | E |
| **The Map** | A visual map of modules, with tools and closet items as pins, and suggested unit trails | module | F |
| Worksheet Generator | Generated practice sheets with answer keys (late roadmap) | module | Late |

## What the site already has (checked 2026-10-26)

- **586 modules** in `data/modules.csv`, about 10 per subject and grade (252 subject-grade rows). Each module lists
  its standard codes at the **cluster** level (`3.NF.A`, not `3.NF.A.1`): 836 distinct codes across CCSS Math and ELA,
  NGSS, C3, NCAS, CSTA, WIDA, NHES and others.
- **Tools map to modules** through `data/tools-concepts.csv` (586 concepts, 74 built, 72 with lesson plans).
- **Standards pages exist**: `/standards/` lists codes by framework, `/standards/<code>/` lists the tools for one code.
  The code pages are noindex "until more tools are built", and most of them show only bench tools today.
- **There are no module pages.** The tool page crumb shows the module title with no link. Every closet shelf is keyed
  to the module, so module pages are the first thing to build (Phase A).
- **Search** (`/search/`) matches every typed word as a substring of the tool's title, module, grade, subject and
  codes. A teacher who types the full code `3.NF.A.1` gets nothing, because the data holds `3.NF.A`.
- **Lesson plans** (`docs/LESSON-PLANS.md`) already end with a timed **Exit check**, and rule 3 already says a
  substitute who has never seen the tool should be able to run the plan. Print CSS for one-page plans is in
  `site/assets/curio.css`.
- **The build** is `scripts/build_site.py` (Jinja2, static, about 1,550 pages, nothing loaded from other hosts,
  checked by `check_site.py`). The Reading Room shows the pattern for a section that stays out of deploy builds until
  it is ready (`--library` flag, `library_live` in templates).

## House rules for everything in the closet

1. **Print first.** Every item prints on US Letter from the browser, black and white friendly (color is a bonus,
   never the only signal), with a small "Curio Class, CC BY 4.0, curioclass.org/..." footer.
2. **Specific or nothing**, as with lesson plans. An item that could belong to any module is not worth printing.
3. **Static.** Built by `build_site.py` from files in the repo. No accounts, no saved data, no outside hosts.
4. **Checked.** Every shelf gets a checker in `scripts/` that the site build runs, like `check_plans.py`.
5. **Words rules** from `docs/agents/STANDARDS.md` and LESSON-PLANS.md rule 7: no em dashes, "Curio Class" never
   "Curio" alone, grade-level language in anything students read, hard history and health guardrails.
6. **Spanish** follows the build plan: anything in Spanish needs a native-speaker review before it goes live. Until
   then it stays out of deploy builds (Q1).
7. **Review tiers** as for tools: Cory reviews every K-2 item and every sensitive one; others are spot-checked about
   one in four, plus anything a checker or verifier flagged.

## Site structure

```
/closet/                         Supply Closet home: the shelves, what's new
/closet/sub-day/                 Every tool that has a Sub Day packet
/closet/word-wall/               Word wall by grade and subject
/closet/anchor-charts/           Anchor charts and posters
/closet/game-night/              Family games by grade and subject
/modules/<module-id>/            NEW: everything for one module (tools, closet items, standards)
/tools/<id>/sub/                 NEW: the Sub Day packet for one tool
/map/                            The Map (Phase F)
```

- **Nav:** "Supply Closet" joins the main nav after Subjects once Phase B ships, gated like the Reading Room until
  then (`--closet` flag, `closet_live` in templates).
- **Module page** (Phase A) is the hub every shelf links into: title, grade, subject, strand, standard codes, its
  tools (built and on the bench), and one row per closet shelf that has something for it. A shelf with nothing yet
  is simply not shown.
- **Tool page:** a **Sub Day** button after **Lesson plan**, and a "Print for this module" line under the Teacher
  notes that links to the module page.

---

## Phase A: Foundation (small, first)

1. **Module pages** at `/modules/<module-id>/` (template `module.html`), in the sitemap once the module has a
   built tool or any closet item, noindex otherwise. Fix the tool page crumb to link to it.
2. **Standards pages point at modules.** `/standards/<code>/` lists the modules for the code first, then the tools.
3. **Search handles full codes.** In `search.html`, a term that looks like a code also matches its cluster prefix
   (`3.nf.a.1` matches `3.NF.A`). Add module pages to `search-index.json`.
4. **Closet scaffold:** `/closet/` home and empty shelf pages behind the `--closet` flag, `closet.html` and a
   `closet` section in `curio.css` print rules (page breaks, the footer).
5. `check_site.py` covers the new pages (links, no outside hosts).

Done when: every tool crumb links to a real module page, `3.NF.A.1` finds Fraction Trail's module in search, and
`build_site.py --closet` builds an empty closet.

---

## Phase B: Sub Day (ships with every new tool)

A one-click packet a teacher prints and leaves on the desk. A skeleton with blanks, not a script.

### The packet (in print order)

| Page | What | Source | New work |
|---|---|---|---|
| 1. Cover | Blanks for the teacher (below), plus the tool's name, URL, a QR code to open it, who drives, minutes, and the steps to open it full screen | template + `tool.json` | none per tool |
| 2. Lesson plan | The existing one-page plan | `plan.md` | none |
| 3. Teacher notes | How each button works | `notes.md` | none |
| 4. Exit tickets | Four tickets per page to cut apart; K-2 gets a class checklist instead | `exit.md` (new) | small |
| 5. Backup sheet | If the tool will not open: a generic "do the worksheet instead" sheet, auto-filled from the module | template + module + plan | none per tool |

**Cover page blanks:** date, class and period times, where the devices and the projector remote are, helpers,
"watch for", what to do with early finishers, where to leave the exit tickets. Lined space, nothing saved online.
Prefilled lines read from `tool.json`: "Students on their own devices" or "You drive it on the big screen", the
minutes, and "If the tool will not load, use page 5."

**QR code:** generated at build time as an inline SVG by a small Python encoder in `scripts/` (no package from the
web, nothing loaded at view time). Q2: worth it, or is the printed URL enough?

### Exit tickets: `tools/<id>/exit.md`

A short structured file, written by the plan agent in the same pass as `plan.md`:

```
kind: ticket            (or "checklist" for K-2)
---
1. Show me: Put 3/4 on the number line. | (between 0 and 1, three of four equal parts)
2. Explain: Why is 3/4 bigger than 2/4? | (same size parts, more of them)
3. Rate it: I can place a fraction on a number line.
```

- 1 to 3 items, written to the student, in the plan's exit check spirit (the plan's **Exit check** and the ticket
  must ask the same thing).
- Grades 3-12: a "show me", an "explain", and a self-rating (1 to 4). Answers in parentheses go on a teacher key strip
  at the bottom of the page, upside down, not on the tickets.
- K-2 (`kind: checklist`): the exit check stays oral or physical, so the page is a class list grid (names left
  blank) with the checks as columns and "got it / almost / not yet" boxes. The sub marks it while calling on children.
- Print: four tickets per Letter page (quarter sheets) with cut lines; one page of checklist for K-2.
- Checker: `check_plans.py` grows an `exit.md` check (kind, item count, answer key present for tickets, words cap,
  no em dashes, the plan's Exit check shares at least one bold term or key word with the ticket).

### The backup sheet (generic fallback)

One template per band that fills itself from the module and the plan, so it needs no per-tool writing:

- **K-2:** "Draw it" box for the module topic, "Show me with your fingers" prompts read aloud by the sub from the
  plan's exit check, and a color-the-faces self rating.
- **3-5 and 6-8:** a frame sheet: what I know about {module title}, two key words and what they mean (from the plan's
  bold terms, later from the Word Wall), one question I still have, then the exit ticket items as written work.
- **9-12:** a short written response built from the plan's goal ("Explain in your own words: {goal}"), the focus
  standard's topic, and the exit ticket items.

When the Word Wall ships, the backup sheet pulls the module's words. When the Worksheet Generator ships (late
roadmap), the backup sheet becomes "print a generated practice sheet for this module" and the generic frame stays as
the fallback for modules the generator does not cover.

### Pages and load

- One page per tool at `/tools/<id>/sub/` (`subday.html`), noindex (its content repeats the plan and notes). Print
  CSS forces a page break between the five parts. The button reads **Sub Day** and is only shown when `exit.md`
  exists.
- 72 tools with plans today means 72 new static pages on a 1,550 page site. Nothing runs on a server and nothing new
  loads at view time beyond one HTML page. The build stays a few seconds longer at most.

### Pipeline change (from now on)

- `docs/agents/PLAN.md`: step 9, write `exit.md` after the plan; report it with the plan.
- `docs/LESSON-PLANS.md`: a "Sub Day" section describing the packet and `exit.md`.
- `scripts/board.py`: a **Sub** column next to **Plan**.

### Backfill

The 72 existing plans get `exit.md` in one batch of plan agents (one tool each, they only write `exit.md`), grouped by
band. Cory reviews the K-2 checklists and the sensitive tools, spot-checks the rest.

Done when: every tool with a plan has a Sub Day button, the packet prints as five clean Letter pages, and new tools
arrive with `exit.md`.

---

## Phase C: Word Wall

### The card

| Field | K-2 | 3-5 | 6-12 |
|---|---|---|---|
| Word | yes | yes | yes |
| Kid-friendly definition | 12 words max | 15 words max | 20 words max |
| Picture | required | required | optional (diagrams for science and math) |
| Example sentence | optional | yes | yes |
| Spanish word and definition | after review (Q1) | after review | after review |

### Data: `data/closet/words/<subject>.csv`

`module_id, word, definition, example, picture, es_word, es_definition, status`

- 5 to 8 words per module. 586 modules means roughly 3,500 cards; 196 modules are K-5, so roughly 1,200 pictures.
- **Source of words:** the bold terms already in each tool's `plan.md` and `notes.md`, the module description, and the
  framework's own wording. An agent drafts a module's list, a checker holds it to the table above.
- **Pictures:** the existing local art pipeline (`scripts/localart.py`), one shared style per band so a whole wall
  looks like a set, with the subject color (`SUBJECT_COLOR`) as the card band. Simple object pictures, white
  background, no text in the image.

### Prints, per module

1. **Wall cards:** two per Letter page, landscape, big type.
2. **Mini cards:** eight per page, for pocket charts, games and word sorts.
3. **My words:** a one-page student glossary with the definitions blank for older grades, filled for K-2.

### Pages

The module page gets a **Word Wall** row; `/closet/word-wall/` browses by grade and subject. Print pages at
`/modules/<id>/words/`.

### Pilot

Grade 3, all subjects (about 40 modules, 250 cards, 250 pictures). Measure minutes per module for words, pictures and
review. Decide the wave size after it, as with tools.

Checker: `scripts/check_words.py` (field caps, word count per module, picture present where required, no duplicate
words in a module, no em dashes, the definition does not use the word itself).

---

## Phase D: Posters and Anchor Charts

### Anchor charts (one per module)

An anchor chart is the module's big idea on one page. Each one is written once as structured text and rendered into
one of a few layouts, so there is no bespoke design work per chart:

| Layout | Fits | Example |
|---|---|---|
| `steps` | a procedure | How to add fractions with like denominators |
| `parts` | a labeled whole | Parts of a plant, parts of a paragraph |
| `compare` | two or three things side by side | Weather vs. climate |
| `cycle` | a loop | Water cycle, the writing process |
| `big-idea` | a statement plus examples and non-examples | What makes a fraction |

**File:** `data/closet/charts/<module-id>.md`, a header (`layout`, `title`), then the parts. Marking a word or line
as `[[blank]]` makes it a blank on the **fill-in** version, so one source gives both versions: **Finished** (to post)
and **Fill-in** (to complete with the class during the lesson; teachers usually build anchor charts live, so this
version may get the most use).

### Posters (a small set per band)

Year-long classroom posters, not per module: number lines and hundred chart, place value, the periodic table, a US
map, a world map, the writing process, the scientific method, the engineering design process, the rights in the Bill
of Rights, and similar. About 10 to 15 per band, roughly 50 in all, chosen by Cory from a proposed list (Q3).

### Printing big

- Every chart and poster is an SVG built by the build script, so it scales cleanly.
- **Sizes:** Letter (one page), **2x2 tiles** (17x22 in, four Letter pages with overlap marks), and **3x3 tiles**
  (25.5x33 in, nine pages). Tiling is the same SVG shown with a different viewBox on each printed page, so no extra
  files.
- A plain "print at a copy shop" PDF is out of scope for now (it would need a PDF step in the build).

### Pilot

The 72 modules that already have a built tool with a plan, so each chart can be checked against a real lesson. Then
waves by band.

Checker: `scripts/check_charts.py` (layout known, part counts per layout, blanks only in fill-in-able places, words
cap per part, no em dashes).

---

## Phase E: Family Game Night

### Scope

2 to 3 games per subject per grade for the four core subjects (math, ELA, science, social studies), K-12. 52 core
subject-grade pairs means about 100 to 150 games. Electives later, only where a game makes sense (Q4).

### The game card (one page; Spanish on the back once reviewed)

- **Header:** title, grade, subject, players, minutes (15 to 20), what you need.
- **How to play:** numbered steps a parent can follow without knowing the subject.
- **What your child is learning:** one or two sentences, plain words, no standard codes.
- **Make it easier / Make it harder:** one line each.
- **Loved it at school?** a link to the matching tool when one is built (shown on both the card and the tool page as
  "Play at home").

### Rules

- **Materials allowed:** paper, pencils, crayons, a deck of cards, dice, coins, a timer, and ordinary household
  objects. Nothing to buy, nothing to print beyond the card itself (a small printable board is allowed as page 2).
- 15 to 20 minutes, 2 or more players, works with one adult and one child.
- No reading needed by the child for K-1 games.

### Data: `data/closet/games/<game-id>.md`

Header: `grade, subject, module_ids, players, minutes, materials, tool_id (optional)`; sections as above.

### Pilot

10 games: one per core subject at K, 3 and 7, plus one wildcard. Cory (and a family or two) play-tests them. Then fill
in by band.

Checker: `scripts/check_games.py` (materials from the allowed list, minutes and players in range, section order,
words cap, no em dashes, K-1 games have no reading step).

---

## Phase F: The Map (last)

### What it shows

- **Regions** are subject and grade pairs (Grade 3 Math). Inside a region, **stops** are its modules, grouped by
  strand (about 10 stops per region, at most 19).
- **Pins** on each stop: a built tool, Sub Day, Word Wall, anchor chart, game. A stop with a built tool is filled in;
  a stop with only planned work is drawn as an outline, so the map doubles as a "what's ready" view.
- **Trails** connect stops in a suggested teaching order for the year, and a dotted line marks "builds on" links to
  the previous grade's region (2nd grade place value leads into 3rd grade rounding).
- Clicking a stop opens its module page.

### Data: `data/sequence.csv`

`subject, grade, module_id, order, builds_on` (builds_on: module ids, semicolon separated, any grade)

The module order in `modules.csv` follows the frameworks' own order, which is not always a teaching order. An agent
drafts `sequence.csv` per subject and grade from the frameworks and common pacing; Cory spot-checks one region per
subject. Q5: should we look at published progressions and pacing guides for reference first, and check their
licenses before leaning on any of them?

### Build

- Drawn at build time in Python as inline SVG (no chart library, nothing loaded from other hosts), one map page per
  subject-grade region (`/map/<subject>/<grade>/`) plus an overview at `/map/` that shows the regions as a grid by
  grade and subject, shaded by how much is ready.
- Keyboard and screen reader friendly: every stop is a real link with its module title, and the region page also
  lists its stops in order as plain text below the map.
- On phones the region map becomes a vertical trail.

### Standards view

The `/standards/<code>/` page shows a small map of where the code's modules sit, with links into the region.

Done when: every module appears on a region map, every region has a trail, and the map's shading matches the build
board.

---

## Late roadmap: Worksheet Generator (parked 2026-10-26)

Agreed as a concept, held until the shelves above are in place. The design so far, so it is ready when its turn
comes:

- **Clicks only.** Pick grade, subject and module (or arrive from a module page), then level (Support / On-level /
  Stretch) and type (Practice / Apply / Quick check). Generate, then Print, with the answer key on page 2. Optional:
  number of items, name and date line, "new set". A **seed code** in the corner brings back the same sheet.
- **3 levels x 2-3 types per module.** The three levels look the same (same layout, same title); a small mark in the
  corner (1, 2 or 3 dots) tells the teacher which is which.
- **Three tiers of content:**

  | Tier | Subjects | How | Share of modules (rough) |
  |---|---|---|---|
  | A. Procedural | math, phonics and spelling patterns, grammar, CS logic, balancing equations | templates with random numbers or words; answers computed | about 30% |
  | B. Fact-based | science, geography, civics | question templates over a fact bank; reuse the data tools already hold (State Quest, Elements Inspector) | about 35% |
  | C. Interpretive | reading, writing, arts, health, SEL, hard history | frame sheets (organizers, sentence starters, claim and evidence) and short curated pools; Reading Room texts as passages | about 35% |

- **One engine, one recipe per module.** The engine (one JS module: the controls, seeded random, print layout, the
  key page) is built once. Each module gets a small recipe file naming its tier, templates and levels.
- **The risk is a wrong answer key.** A checker generates many seeds per recipe and verifies every key (exact for
  Tier A, fact-bank lookups for Tier B, human review for Tier C).
- **Pilot when it starts:** one grade of math (Tier A), then one Tier B and one Tier C module. Time a recipe in each
  tier before committing to all 586 modules. If Tier C is too slow, frame sheets alone cover those subjects.
- **Hooks already planned:** the Sub Day backup sheet and the module page both get a "generate a sheet" link when it
  ships.

---

## Order and dependencies

```
A Foundation ──> B Sub Day ──> (ships with every new tool from here on)
            ├──> C Word Wall ──┐
            ├──> D Charts ─────┼──> F The Map ──> Late: Worksheet Generator
            └──> E Game Night ─┘
```

- A comes first: every shelf needs module pages and the closet scaffold.
- B comes next: it is small, uses what exists, and starts riding along with each new wave of tools.
- C, D and E are independent of each other once A is done. Suggested order C, D, E (the Word Wall also feeds the Sub Day
  backup sheet and the fill-in charts), but they can overlap, one pilot at a time.
- F is last because its pins are worth more once the shelves have content.
- The Supply Closet joins the main nav when B ships.

## Pilots and what they measure

| Phase | Pilot | Measure before scaling |
|---|---|---|
| B | Sub Day for 10 tools across bands, then the backfill | print quality on a real printer, minutes per `exit.md`, Cory's send-back rate |
| C | Grade 3 word wall, all subjects | minutes per module (words, pictures, review), picture reject rate |
| D | Anchor charts for the 72 modules with plans | which layouts cover which subjects, tile print alignment |
| E | 10 games | play-test notes, how often a game needed a rewrite |
| F | Grade 3 regions for the four core subjects | does the trail read right to a teacher, phone layout |

## Open questions for Cory

- **Q1.** Spanish: launch the Word Wall and Game Night in English first and add Spanish after a native-speaker review,
  or hold them until both languages are ready?
- **Q2.** QR code on the Sub Day cover: worth building, or is the printed URL enough?
- **Q3.** Posters: approve a proposed list of about 50 before any are made?
- **Q4.** Game Night: core four subjects only at first, or include electives (arts, health and PE, CS) from the start?
- **Q5.** The Map's teaching order: research published progressions and pacing guides first (license check), or
  draft from the frameworks alone?

## Decisions (Cory, 2026-10-26)

- Name: **Supply Closet**.
- Worksheet Generator: agreed as a concept, moved to the late roadmap.
- Sub Day comes with each new tool. The packet is: cover page, lesson plan, teacher notes, exit ticket sheet, and a
  generic "do the worksheet instead" fallback.
- Word Wall, Posters and Anchor Charts, and Family Game Night (2-3 per subject per grade): agreed as concepts.
- The standard-to-tool visual map is the last piece, tied to unit sequencing.

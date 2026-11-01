# Worksheets: printable practice sheets (plan)

Status: CONCEPT LISTS, started 2026-11-01 (Cory). Track 2, Supply Closet, item 6 in docs/ROADMAP.md. Nothing is built
or on the site yet.

## What it is

A Supply Closet shelf of print-ready student worksheets a teacher can hand out tomorrow: **40 to 50 per class**, for
every class Curio Class covers, K-12. Each worksheet is hand-designed around one skill or idea from a module, prints
on US Letter in black and white, and comes with a teacher page (answer key and notes).

This is not the parked Worksheet Generator (docs/SUPPLY-CLOSET-PLAN.md, "Late roadmap"). The generator makes endless
random practice from templates; these are authored sheets, each one designed. The two fit together later: an
authored sheet can carry a "more like this" link to the generator for its module when the generator exists.

## A class is a unit

Cory chose "by class" (2026-11-01): a list for each class a teacher actually teaches.

| Subjects | One unit per | Units |
|---|---|---|
| ELA, Health, PE, Visual Arts, Music, Theater, Dance, Media Arts, Computer Science, SEL, ELD, Library | grade, K-12 | 156 |
| Math, Science, Social Studies | grade, K-8 (grade 6-8 Social Studies is its course: World Geography, World History, US History to 1877) | 27 |
| High school courses | course: Algebra I, Geometry, Algebra II, Precalculus, Statistics, Calculus; Earth and Space, Biology, Chemistry, Physics, Environmental; World History, US History since 1877, Government, Economics, Psychology | 16 |
| CTE | grade 6-8 (Career Exploration), then course: Career Pathways, Personal Finance | 5 |
| World Languages | proficiency level, not grade: Spanish and ASL Novice (K-5), Novice (6-12), Intermediate, Advanced; French Novice, Intermediate, Advanced | 11 |
| **Total** | | **215 units, about 9,700 worksheets** |

`python scripts/check_worksheets.py --units` lists them all; `--modules <unit-id>` lists the modules a unit covers.
The units come from `data/courses.csv` and `data/modules.csv`, so a new module shows up in its units automatically.

## The concept lists

`docs/worksheets/<subject>.md`, one file per subject (Arts split by discipline, Health and PE split). Each unit is a
section, in course order:

```
## ela-3: Grade 3 English Language Arts

| # | Worksheet | Type | Module | Students |
|---|---|---|---|---|
| 1 | Who Is Telling? Point of View Sort | Practice | Point of View | Sort 12 short passages by narrator (first or third person), then rewrite one from the other view. |
```

- **Worksheet:** a specific, teacher-friendly title. Never "Fractions Practice 2".
- **Type:** one of the types below.
- **Module:** the module title from `data/modules.csv` (the sheet links to its module page, and through it to the
  standards, tools, Word Wall and chart). "-" only for a unit with no modules yet (French).
- **Students:** what students actually do on the sheet, in one sentence (6 to 30 words), concrete enough that a
  writer can build the sheet from it.

### Rules for a unit's list

1. **40 to 50 sheets.** Every module in the unit gets at least 2, and roughly in proportion to its size.
2. **In teaching order:** the order a teacher would use them across the year, module by module, with a few review
   sheets at natural checkpoints.
3. **A real mix of types.** At least 4 types per unit, no type over 60%. Math leans on Practice and Apply; history on
   Source analysis, Timeline and Map; science on Lab, Diagram and Data and graphs; arts on Critique, Planner and Log.
4. **Grade-right.** K-1 sheets are mostly pictures, tracing, circling, cutting and gluing, and drawing, with a few
   words a teacher reads aloud. Reading load grows with the grade.
5. **Distinct.** No two sheets in a unit do the same thing. Consecutive grades build on each other rather than
   repeating (grade 4 fractions are not grade 3 fractions).
6. **Paper is the product.** Nothing needs a device. Sheets that pair with a Curio Class tool say so in the Students
   line ("after the tool", "while using").
7. **No busywork.** Word searches and coloring-only sheets are out. A Puzzle sheet must make students use the
   skill (a cross-number with real computation, a logic grid built on the content).
8. **Vocabulary sheets sparingly** (at most 3 per unit): Word check on the Word Wall shelf already does matching.
   A Vocabulary sheet here does something more (sort, use in context, draw it, word map).
9. **House rules:** no em dashes, "Curio Class" never "Curio" alone, hard history and health guardrails
   (docs/agents/STANDARDS.md), and nothing that needs a student's personal or family information.

### Types

| Type | What it is |
|---|---|
| Practice | Focused skill practice with a worked example at the top |
| Apply | Word problems, scenarios or real-world tasks that use the skill |
| Read and respond | A short passage (original, or public domain) with questions |
| Organizer | A graphic organizer: Venn, cause and effect, story map, claim and evidence |
| Diagram | Label, draw or complete a diagram |
| Data and graphs | Read, make or interpret a table, chart or graph |
| Lab | Record sheet for an experiment or investigation: question, prediction, data, conclusion |
| Map | Map reading, labeling or making |
| Timeline | Build or read a timeline, sequence events |
| Source analysis | Read a primary or secondary source (text, image, chart) with guiding questions |
| Writing frame | Scaffolded writing: sentence starters, paragraph frame, outline |
| Vocabulary | Use words in context, sort, word maps, draw it (not plain matching) |
| Review | Mixed review or quick check across a module or several |
| Planner | Plan a project, performance, design or investigation |
| Reflection | Self-assessment, goal setting, journaling prompt |
| Log | Practice log, fitness log, listening log, observation log over time |
| Critique | Look at a work (art, performance, code, writing) and respond with criteria |
| Puzzle | Logic puzzle, cross-number, code, riddle that requires the skill |

## The sheet (for when they are built)

Not part of the concept lists; this is the layout every built sheet will share.

**Student pages (1 or 2 Letter pages):**

1. Header: Name, Date, Class lines; the worksheet title; grade and subject in small type.
2. **I can** line, from the module.
3. **Directions** in plain words. K-2 directions are short, with a small picture, and the teacher reads them aloud.
4. **Example** box: one worked example or model answer (Practice, Apply, Writing frame).
5. **Part A, warm up:** 2 to 4 easy items.
6. **Part B, main:** the core of the sheet, 6 to 12 items or one extended task.
7. **Part C, stretch:** 1 or 2 harder or open items.
8. **Check yourself:** a short self-rating ("I can do this: on my own / with help / not yet").
9. Footer: "Curio Class, CC BY 4.0, curioclass.org/..." like every closet item.

**Teacher page:** answer key (or a model answer and a short rubric for open tasks), the module and its standard
codes, time (10 to 30 minutes), materials (scissors, glue, crayons), the tool it pairs with, and one line on common
mistakes to watch for.

**Data:** one file per sheet, `data/closet/worksheets/<unit-id>/<nn>-<slug>.md`, `key: value` header lines (title,
type, module, minutes, pairs) then the parts, like the other closet shelves. A checker verifies every answer key
(computed for math, looked up for facts, a human pass for open answers).

## Order (proposed)

1. **Concept lists** for all 215 units (this step). Cory reviews the lists.
2. **Pilot:** about 10 built sheets across bands and types (one K math, one grade 3 ELA, one grade 7 science lab, one
   high school history source analysis, and so on) to set the build format, the print CSS and the time per sheet.
3. **Build waves** by subject and band, core subjects first, with the answer-key check.
4. **Site:** `/closet/worksheets/` by grade and subject, a sheet page that prints the student pages, and a separate
   teacher page with the key (the key never prints on the student copy). Module pages get a Worksheets row.
5. **Spanish** for the student pages, then the native-speaker review (closet rule 6).
6. **Held collections** keep their holds: ASL sheets wait for the ASL design decision, hard history sheets get the
   fresh review, Spanish-language sheets the native review.

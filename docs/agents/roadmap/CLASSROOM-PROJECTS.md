# Classroom projects by standard (future roadmap input)

Cory added two notes on 2026-10-27 for later use. **They do not change current work** (idea pass, catalog audit,
wave builds). Read them when a roadmap item about offline classroom projects starts.

## Sources

- `S:\Notes\Classroom_Projects_by_Standard.json` (11.7 MB): the data.
- `S:\Notes\Classroom_Projects_by_Standard.md` (8.5 MB): the same content as a readable teacher reference.

Both live outside the repo. Copy them in only when a roadmap item uses them.

## What they are

"Classroom Projects for Every Standard in the Curio Class Collection", created 2026-10-27. It has 3,811 entries: all
3,675 codes in the standards reference lists plus 136 extra curriculum codes. Each entry is a hands-on classroom
project (no screen needed) for one code.

The JSON has top-level `title`, `created`, `total_entries`, `framework_counts`, `focus_note` and `projects`. Each
project has:

- the code: `standard_code`, `section`, `framework_group`, `grade_or_proficiency`, `standard_focus`;
- the project: `project_title`, `project_format`, `room_layout`, `suggested_time`, `materials`;
- `project_lines`: 9 labeled steps (Launch, Set up, Investigate, ... with a check of learning);
- where it came from: `source_collection_file`, `framework_source`, `focus_basis`, `source_page`, `presentation`.

Counts by framework: arts 1257, ela 455, finance 385, social 283, pe 214, science 208, cs 196, health 180, math 157,
wida 113, cte 100, hecat 91, library 74, sel 45, language 26, ap 21, psych 6.

## Caveats

- Only 191 distinct project titles cover all 3,811 entries. Templates repeat across codes; for example, "The Community
  Service Design Fair" appears 100 times. Treat the entries as starting frames to adapt, not finished one-per-code
  projects.
- The focus lines are the author's summaries, not official standard wording (the file says so itself).
- Math entries are at cluster level (`K.CC.A`), the same level as data/modules.csv.

## How it could feed Curio Class later

- **Supply Closet shelf "Projects":** an off-screen project on each module page, paired with the module's tool, for
  classes without devices. Rewrite each entry to the site's voice and rules before it is published.
- **Lesson plan extension:** the plan's "Short on time" and "Support and stretch" sections could link to the
  module's project as a follow-up day.
- **Coverage backstop:** where a code has no tool yet, or a MOVE leaves it homeless for a while, the project shows
  teachers one way to teach it. It never replaces a tool under BASELINE rule 2.
- **Catalog audit input:** the per-code focus lines and formats can suggest tool ideas for gap codes (for example,
  the 41 CCSS-ELA codes with no tool).

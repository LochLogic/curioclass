# Gap fill: brief for the domain agents (2026-10-27)

Cory asked to fill the standards gaps "smartly and completely" and is open to new tools. Start from
`docs/agents/overlap/wave1-gaps.md`, which measures coverage against the full official lists and names the gaps.

## The goal

Every code on the official lists for your frameworks is claimed by at least one tool, except codes you leave out
**by design**, each with a one-line reason in your notes (for example RL.10, "range of reading", is not a one-tool
skill). Do it with as few new tools as a good catalog allows, and with no tool that is only a code sweep.

Work in this order:

1. **Code adds to existing modules (cheapest).** Add a code only where the tool already does the work. Read the
   tool's concept line (data/tools-concepts.csv); for a specced tool read tools/<id>/spec.md; for a live tool
   (tools/<id>/tool.json exists) read its spec.md. A teacher reading the code's wording should agree the tool
   practices it. When you add a code to a **specced, not live** tool's module, also append the code to that spec's
   `- Standards` line so spec and module stay in step.
2. **New modules, one new tool each, for what is left.** Make each tool carry a coherent set of codes:
   - A module's grade may span a band (`3-5`, `6-8`, `9-10`, `11-12`, `9-12`) when the course allows it. A span
     module carries the grade-level code for every grade it spans (`RL.3.1;RL.4.1;RL.5.1`), and the tool has a grade
     or level switch.
   - One skill per tool, with up to about three closely related standards per grade. Pairing standards a teacher
     teaches together is smart (theme with citing evidence); bolting on unrelated ones is not.
   - Spread new tools across bands and formats; vary actions and worlds.

## What you write (only in your folder, docs/agents/gapfill/<domain>/)

- `codes.txt`: `module_id: CODE; CODE  # reason (tool id, what it already does)`. `-CODE` removes a wrong code.
- `modules.txt`: `source.txt|grade|course|strand|title|description|standards`. source.txt is the data/modules file the
  line belongs in: ela.txt, math.txt, science.txt, social-studies.txt, electives.txt (arts, CS, CTE, health-pe, SEL,
  world languages), added.txt (eld, library, ASL). Courses and their grade spans are in data/courses.csv (media-arts
  is now k-12). The module id becomes `<subject>-<grade>-<slug of title>`.
- `concepts.txt`: one line per new module, `module_id|Tool Title|format|family|concept`. Formats: data/formats.csv.
  Family: an existing family from data/tools-concepts.csv when the tool shares its engine, else a new short name or
  blank.
- `tags.csv`: one row per new tool with the header of docs/agents/overlap/tags.csv:
  `tool_id,title,band,subject,live,format,family,skill_key,skill,action,setting_group,setting` (live is `n`; band is
  K-2, 3-5, 6-8, 9-12, K-12 or 6-12; action from the fixed list in docs/agents/overlap/method.md).
- `notes.md`: what you added and why, the codes left out by design with reasons, anything Cory should decide.

Check as you go: `python scripts/overlap/stage_check.py docs/agents/gapfill/<domain> --missing`. It validates
everything above, runs the clash rule against the catalog, flags crowded settings and overused title words, and
prints the coverage your folder would reach. Finish with zero ERROR lines; judge each warning and say in notes.md
why any that remain are fine.

## Concept rules (from the overlap pass and earlier waves)

- Match the existing concept style: one or two sentences, present tense, what the class or student does in the
  tool and what they find out. About 25 to 45 words. Read 20 concept lines in your subject first.
- Curio Class tools are short interactive web tools a teacher projects or students use, K-12, free. The class or a
  student acts; the tool responds.
- **Titles:** a plain name with the topic word in it (Fair Use Review, Chore Flowcharts). No trademarks or product
  names. No "Detective", and avoid words already used 5 or more times (the checker lists them). Unique catalog-wide.
- **Overlap rule:** within a band, two of skill key, action and coarse setting matching another tool is a clash.
  Live tools never move, so your tool moves. Crowded settings to avoid: 9-12 lab, business and money, council and
  debate; 6-8 travel map; K-2 town, robot and machine; 3-5 nature. A tool in a world already used in the band should
  have a different skill and action.
- No em dashes or en dashes anywhere. Write "Curio Class", never "Curio" alone.

## Do not

- Do not edit data/, docs/agents/overlap/, the concept files, or anything outside your folder, except the
  `- Standards` line of a specced tool's spec.md as above. I merge the folders.
- Do not touch game-remix or code-tracer (or their modules), and do not commit, build or deploy.
- Do not invent codes: every code must pass the checker, which uses the official lists in data/standards/.

## Domains

- **ela:** CCSS ELA (all strands, K-12) and the empty WIDA language-use cells (ELD modules, added.txt).
- **social:** C3 all four dimensions (D1 questions, D2 civics, economics, geography, history, D3 sources, D4
  communicating and taking action), NSPFE personal finance in grades 3-5, 6-8 and 9-12, and AASL (library).
- **cs:** CSTA 2026 (computing and society and data first), plus CTE where it touches CS.
- **arts-health:** NCAS anchors in all five arts disciplines (media arts K-5 now allowed), NHES, SHAPE, CASEL, and
  the health topic holes in wave1-gaps.md section 7 (substance use 9-12, bullying K-5, safety 3-8, mental health 3-5).
  Sexual health past puberty is Cory's call: do not add it, list it as a question.

Math and NGSS holes and the malformed math codes are handled in the main session.

# Catalog extract brief

You write one row per Curio Class tool for the catalog review (docs/agents/CATALOG-REVIEW.md, step 1). You read and
report. You change nothing else, judge nothing as good or bad overall, and do not commit.

## Do this

1. Read your packet, `docs/agents/catalog/batches/<packet>.md`. It lists each tool, its module, the module's standards,
   its old tags and the files to read.
2. Read the listed files for every tool. Read several files in one call where you can. For a built or live tool do not
   read src.html; the spec, notes.md and tool.json are enough.
3. Write `docs/agents/catalog/rows/<packet>.jsonl`: one JSON object per line, one line per tool, in packet order.
4. Report in under 15 lines: how many rows, and anything in a spec that made a field hard to fill.

## The row

```
{"id": "", "module": "", "stage": "",
 "codes": [{"code": "", "depth": "", "activity": "", "where": ""}],
 "module_codes_untaught": [""],
 "skill_key": "", "skill": "", "action": "", "setting_group": "", "setting": "",
 "kinds": {"understanding": 0, "fluency": 0, "application": 0},
 "screen_adds": "", "paper_gap": "", "texts": [], "grade_split": "",
 "use": "", "minutes": 0, "cost_class": "",
 "beatable": [""], "flags": [""], "unsure": [""]}
```

- **codes:** every standard the spec says it teaches (its "Standards map" table, and any code named elsewhere), at the
  finest level the spec names (4.NBT.5, not 4.NBT.B). One entry per code, with these fields (row format 2, 2026-11-10,
  after the pilot: add them to each entry beside `code`, `depth`, `activity`, `where`):
  - `parts_missing`: read the standard's own wording (you know the Common Core and NGSS texts; say in `unsure` if you
    are not sure of a wording). List each part of it the student never does here: a kind of number, an operation, a
    case, a lettered sub-part, "explain why", "write", "record with symbols". Empty list only if every part is done.
  - `verb`: the standard's own verb in a word or two (solve, explain, compare, write, investigate).
  - `key_step`: judged by that verb. `student` if the student does the step the standard is about, `tool` if the tool does it and the
    student watches or presses on, `shared` if the student chooses and the tool carries it out.
  - `items`: how many problems, rounds or texts the student meets for this code on the main path (0 if not stated).
  - `support`: `modeled` (a worked model or example is shown), `guided` (hints or a guide while working), `none`.
  - `check`: `tool-key` (right and wrong answers), `tool-rule` (a rule the tool can test, such as "quotes the text"),
    `self-guide` (the student checks against a shown guide), `teacher`, `none`.
  - `on_path`: true if a student who just follows the tool meets it; false if it sits in an optional mode or the notes.
  - `depth` is one of:
    - `taught`: on_path, key_step is student or shared, there is support, and a check other than none that cannot be
      passed by guessing or by letting the tool do it. For writing and talk, a self-guide check on screen counts;
    - `practiced`: the student does it, but with no model or guide, or with no check;
    - `explored`: only for a standard whose verb is understand, use a model or investigate (never solve, write,
      compute or prove): the student sets up cases and predicts before each reveal. Add `unit_adds`: one line on
      what a unit must add for the standard to be taught in full;
    - `shown`: the tool does the key step; the student watches;
    - `touched`: not on the main path, or can be skipped;
    - `claimed`: the code is listed and nothing the student does matches it.
    A code whose only check is listed in `beatable` cannot be `taught`.
  - `activity`: what the student does, in ten words or fewer, in the spec's own terms.
  - `where`: the spec section or mode that shows it.
  Judge from what the spec says the student does, not from the claim in the table.
- **module_codes_untaught:** when the module lists a cluster (4.NBT.B) or several codes, name the standards inside it
  that this spec does not teach or practice. Use the standard's usual number (4.NBT.4). Empty list if none.
- **skill_key, action, setting_group:** keep the packet's old tags when they still fit the spec; change one only when
  the spec clearly differs, and say so in `unsure`. `action` is one of: count-along, move-along, predict-reveal, sort,
  match, order, build, compose, manipulate, simulate-tune, experiment, explore, hunt, solve, fix, investigate,
  annotate, drill, choose-path, debate, converse, manage, care-for, analyze-data, locate, discuss, rehearse, trace,
  plan, program, compare. `skill` is one plain line; `setting` is the picture or world in a few words.
- **kinds:** how much of the student's time goes to each, 0 to 3 (0 none, and 0 is the default, 1 a little, 2 a real part, 3 most of it):
  `understanding` (seeing why it works, models, explaining), `fluency` (getting quick and accurate at a procedure),
  `application` (using it on a real or story problem where the student must decide what to do).
- **screen_adds:** what this tool does that a worksheet, a card game or a teacher at the board could not, in one
  sentence. Say "nothing clear" if that is the case.
- **paper_gap:** the one thing a printed sheet with a teacher could not do here, named plainly, or "none".
- **texts:** for reading and writing tools, each text used: `{"title": "", "source": "written for the tool | public domain | excerpt", "words": 0}`. Empty list otherwise.
- **grade_split:** for a tool that claims more than one grade: `different-task`, `different-content`, `same-plus-step` or `one-path`; "" for a single grade.
- **use:** `lesson` (carries a whole class period), `station` (practice after teaching), `demo` (a short
  teacher-led look) or `ongoing` (returned to over days).
- **minutes:** the time one sitting takes, from the spec; 0 if it does not say.
- **cost_class:** `simple`, `sibling` (reuses a family engine that exists), `new-engine` or `super`, from the spec's
  Family engine, Art and Screens sections.
- **beatable:** checks, scores or win states a student could pass without the skill that the spec's "Can it be
  beaten?" section does not already close. List one only when trial is cheaper than thinking: few choices, or
  feedback that says which way to move, with free tries. Trying again is not beating a check where the standard
  itself asks the student to design, refine or investigate. A partner or teacher marking a read-aloud is a real
  check. Empty if none found or the tool has no checks.
- **flags:** any of `k2-guess-prompt` (a K-2 reading tool that tells a child to guess a word from the picture or the
  sentence rather than sound it out), `sensitive` (cultural, Native, hard history, health), `facts-unsourced` (claims
  with no entry in Sources), `spec-thin` (a section the row needed is missing or one line).
- **unsure:** anything you guessed, in a few words each. Better to list it than to hide it.

## Rules

- Each row comes only from that tool's own files. Do not carry an impression from one tool to the next.
- Put findings in the fields, not only in `unsure`: a missing part goes in `parts_missing`, a hole in `beatable`.
- For a built or live tool, the spec may be old or missing. Use notes.md, tool.json and plan.md, and search src.html
  (grep, never a whole read) to settle what the student really does.
- Be literal and strict about `depth`. Most errors a later reader finds are a `touched` written as `taught`.
- Plain words. No em dashes. "Curio Class", never "Curio" alone.

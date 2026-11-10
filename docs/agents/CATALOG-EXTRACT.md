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
 "screen_adds": "", "paper_version": "",
 "use": "", "minutes": 0, "cost_class": "",
 "beatable": [""], "flags": [""], "unsure": [""]}
```

- **codes:** every standard the spec says it teaches (its "Standards map" table, and any code named elsewhere), at the
  finest level the spec names (4.NBT.5, not 4.NBT.B). One entry per code.
  - `depth` is one of:
    - `taught`: on the default path the student does something that needs the skill, and the tool's response depends
      on whether they did it right;
    - `practiced`: the student repeats the skill, but the tool assumes it was taught elsewhere (no model, no
      explanation, no feedback beyond right or wrong);
    - `touched`: the skill appears, but a student can finish without using it, or it sits only in an optional mode,
      a teacher prompt or the notes;
    - `claimed`: the code is listed and nothing the student does matches it.
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
- **kinds:** how much of the student's time goes to each, 0 to 3 (0 none, 1 a little, 2 a real part, 3 most of it):
  `understanding` (seeing why it works, models, explaining), `fluency` (getting quick and accurate at a procedure),
  `application` (using it on a real or story problem where the student must decide what to do).
- **screen_adds:** what this tool does that a worksheet, a card game or a teacher at the board could not, in one
  sentence. Say "nothing clear" if that is the case.
- **paper_version:** `none`, `partial` or `full`: how much of what it teaches a printed sheet could teach as well.
- **use:** `lesson` (carries a whole class period), `station` (practice after teaching), `demo` (a short
  teacher-led look) or `ongoing` (returned to over days).
- **minutes:** the time one sitting takes, from the spec; 0 if it does not say.
- **cost_class:** `simple`, `sibling` (reuses a family engine that exists), `new-engine` or `super`, from the spec's
  Family engine, Art and Screens sections.
- **beatable:** checks, scores or win states a student could pass without the skill that the spec's "Can it be
  beaten?" section does not already close. Empty if none found or the tool has no checks.
- **flags:** any of `k2-guess-prompt` (a K-2 reading tool that tells a child to guess a word from the picture or the
  sentence rather than sound it out), `sensitive` (cultural, Native, hard history, health), `facts-unsourced` (claims
  with no entry in Sources), `spec-thin` (a section the row needed is missing or one line).
- **unsure:** anything you guessed, in a few words each. Better to list it than to hide it.

## Rules

- Each row comes only from that tool's own files. Do not carry an impression from one tool to the next.
- Be literal and strict about `depth`. Most errors a later reader finds are a `touched` written as `taught`.
- Plain words. No em dashes. "Curio Class", never "Curio" alone.

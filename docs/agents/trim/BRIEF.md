# Brief: propose which planned worksheets to cut (Curio Class, 2026-11-04)

Curio Class (S:\CurioClass) plans 40 to 50 printable worksheets per unit (a class, such as music-3) in
docs/worksheets/<subject>.md. Cory decided (Review Desk, 2026-11-04) to trim each unit to about 30 hand-written
sheets, keeping the strongest and most varied, with generator-made sheets on top of that. You propose the cuts.
Nothing is removed until Cory has seen the list.

## Inputs

- `docs/agents/trim/input/<subject>.csv`: every planned row, with `status`:
  - `written`: already written by hand. Never cut.
  - `generated`: a Worksheet Generator makes it. Never cut; it does not count toward the 30.
  - `open`: not written yet. Only these can be cut.
- `docs/agents/trim/input/units.csv`: per unit, `cut_target` = how many open rows to cut so written + kept open
  rows come to 30. Hit it exactly, or within 2 when a cut would break a rule below (say why).

## How to choose (in this order)

Read each row's Students line and judge it; a script may only count. In a unit with more than 10 modules, a module
may go down to 2 sheets (rule 3), still keeping its end Review.


1. Cut repeats first: a third or fourth Review sheet in a unit, near-duplicate Practice or Apply rows in the same
   module that ask students to do the same thing on different content, a second Log or Reflection that repeats a
   first, and open rows that a `generated` row in the same module already covers.
2. Then the weakest: rows that are thin (a vague Students line), that need materials a typical class lacks, or that
   teach something already taught well by another kept row.
3. Keep coverage: every module keeps at least 3 sheets in all (written + generated + kept open), and its end-of-module
   Review if it has one. Keep the unit's spread of types (do not cut the only Lab, Map, Source analysis, Critique,
   Puzzle, Writing frame or Data sheet in a unit). Keep any row that is the only one teaching a standard or big idea.
4. Keep the stand-outs: rows with a memorable hook, a real source or named work, or an activity students enjoy.
5. K-2 units: keep the simple hands-on picture sheets over the wordy ones.

## Output

For each subject file, write `docs/agents/trim/<subject>.csv` with header `unit,n,title,type,module,reason`, one line
per row to CUT (reason: 4 to 12 words, naming the kept row it repeats when that is the reason, for example "repeats
n12 Rhythm Detective"). Then reply briefly: per unit, the cut count against the target (only list units that miss
it, with why), and anything a reviewer should look at. No em dashes anywhere. Edit nothing else in S:\CurioClass.
Do not commit.

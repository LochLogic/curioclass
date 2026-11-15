# Unit skeleton spot check: fixes applied, 2026-11-15

This follows up `docs/reviews/skeleton-spot-check-2026-11-15.md`. Every finding below is marked either applied, with the function and what changed, or not applied, with the reason.

The script is `scripts/unit_skeleton.py`. Every script change is gated to math, ELA and science (`not is_ss()` or `subj != 'social-studies'`). The social studies skeletons are frozen: after each change, all 138 were regenerated to a scratch folder and diffed against the baseline, and the result was identical every time.

## Across the sample

### Script findings

1. **Earlier-grade skills treated as owned.** Applied.
   - `build()` splits the skills column into own-grade rows (`own_sk`) and earlier-grade rows (`early_sk`).
   - "Progression skills owned" lists only own-grade rows. A new field 2 line lists the earlier-grade rows as retrieval or readiness, not owned.
   - "Builds on" and "Leads to" come from own-grade rows only. "Leads to" also drops rows already taught earlier in the course, such as unit 1 rows, and any earlier-grade rows.
   - The field 10 Note now uses own-grade rows. A code cited through its lettered parts, or a part cited through its parent, counts as cited.
   - In `earlier_rows`, the assumes list for math, ELA and science is now:
     - earlier-grade ids in the skills column;
     - plus the assumes of own rows not already cited earlier in the course;
     - plus earlier-grade ids named in the unit's tasks.

     Geometry s03 now lists all four day 48 readiness rows.
2. **Continuous use becomes a retrieval TODO.** Applied, in `earlier_rows`. A same-year retrieval row with no task naming it is now marked "in use this year (no task by id needed)" and gets no TODO. The "not named by id" count is now 0 in each of ELA 3, ELA 7, ELA 11 and math 1.
3. **`retrieval_clauses` junk.** Applied. Math, ELA and science now use new helpers, `task_clauses` and `unit_tasks`.
   - Clauses are taken whole, so ids are no longer cut off (math 5 day 49, chemistry).
   - These are dropped:
     - rules containing "never";
     - mentions of a task on another day;
     - minute budgets and routines with no reference;
     - reviews of the unit's own days.
   - "instead of / replacing ... retrieval" is not a task.
   - "Refresh <id>" counts as a task (science 4 day 18).
   - A clause "for unit N" or "for the next unit" is credited to that unit. So are next-unit ids on the last three days (ELA 7 day 86, geometry day 67).
   - Readiness-window clauses written for this unit, on days before it starts, are credited to this unit.
4. **Compelling question lost.** Applied. `split_unit_cell` now uses `split_science_cell` for math, ELA and science. That function handles these shapes:
   - italic questions;
   - a quoted question after a title that itself ends in "?";
   - "Title: Question?";
   - `**Title** (weeks ...)` and `(about ...)`;
   - bracketed asides after the "?".

   93 titles changed. All were checked by hand.
5. **The ~ (begun) mark.** Applied, with a new helper `begun_codes`. A code is begun when any of these holds:
   - days.csv writes it with ~;
   - the progression marks it ~ on an own row and no own row owns it bare;
   - a note says "unit N completes" and the frame's Owned standards for the unit do not list it.

   Begun codes show as `~code (begun here; <where completed>)` in field 2. The Limits TODO names them. Field 5 carries the begun mark in the Part cell, and the code cell shows the raw days.csv form. The day list prints the raw codes. This covers ELA 11, geometry G-CO.C.10 and G-MG, and math 8 8.EE.B.6.
6. **Field 5: kept evidence and coverage.** Applied in `build()`, with helpers `evidence_days`, `reuse_sources`, `mentions` and `coverage_gaps`.
   - A line lists the teaching days whose product is kept as evidence.
   - Codes the note reuses get the owner "reused from day N (no new item; name the record)". This covers math 5's "7c" and "for 6", math 8 day 34, geometry day 65 and math 1.
   - Codes the note marks as contributing evidence get the owner "contributing evidence only".
   - The Time line adds the minutes the note budgets (math 8 day 28, science K day 28).
   - A coverage line and a TODO now list owned codes that appear on no assessment day and no kept day.
   - The parent row is kept, not dropped, and pre-filled with "Asked through the part rows below; no separate item". The reason is that `scripts/unitplan.py` requires a field 5 row for every code days.csv cites.
7. **Bulk.** Applied.
   - Field 5 points to the note in the day list instead of reprinting it.
   - Field 10 prints one line per source-map row (source, title, our days, decision, plus an order-conflict flag).

   ELA K to 2 came down to about 60 percent, not half. The day list, which holds each note once, is 9,812 of ELA K's 16,269 words. Halving the file would mean dropping notes the writer needs, so I left them.
8. **Small wording fixes.**
   - The science field 10 TODO is now grade-banded through `base_text_of`. Applied.
   - K-2-ETS1-1 crosscutting: `pe_row` now says "None listed for this engineering expectation" and points to the focal concept. Applied.
   - The hook names the unit's first day. Applied.
   - The hook and Storyline overlap: removed the science "supq" line and reworded the Storyline TODO. Applied.
   - `frame_models` now says "used again here (first used in unit N)" or "reactivated here (from an earlier grade)". Applied.
   - `group_column` merges items by `item_key`, which ignores case, bracketed asides and plural endings. Applied. "spoon" and "metal spoons" stay separate, because merging different wording would need judgment.
   - `SAFEWORDS` no longer matches "chemical". Applied. "harm" was never in the pattern. Other weak tool and safety hits were left alone: they are pointers to the day list, not claims.
   - `used_on` no longer counts a Respond, Check or C day as a one-hop use. Applied. Science 4's sk-sun-warms now reads grade 1, last day 42, because grade 1 days 38 to 42 teach s1-see-with-light. That is a real one-hop use under the lead's rule, and the outcome (readiness) is unchanged.
   - The Weight line spells out "wap". Applied.

### Per-unit extras

- **Applied:**
  - Science 4 finding 2 (Refresh row): see finding 3.
  - Header: "school days N to M" now says how often the course meets when the span holds more school days than course days.
  - A TODO now flags any section longer than 15 days.
- **Not applied:** math 5 finding 5 (the 7a and 7b verb parts). The standards data has no part rows for them, and inventing them is out of scope.

## Data fixes

- **science-kindergarten** `frame.md`: added the full stop before "Anchor:". Also in the script: a design sentence is followed by "Anchor:".
- **science-grade-7** `days.csv`: days 93 and 94 now have assess=end. `end` is a valid value in sequence-write.md.
- **science-grade-4:**
  - Removed the collision clause from the day 36 note.
  - The frame check-set cell now reads "Candidate kept (day 34, one day): ...".
- **english-language-arts-grade-11** `days.csv`: restored the ~ on every unit-row code the frame marks begun. That is 41 codes across 148 rows. Course-level C rows were left bare. A backup is in the scratchpad.
- **geometry** `frame.md` unit 3 "What students learn": now names G-CO.C.10 (midsegment only), and G-MG.A.2 and G-MG.A.3 (begun on days 65 to 66, owned in unit 5). Owned standards are unchanged, as frame.py requires.
- **english-language-arts-kindergarten** unit 4 sections: not changed. The scope sets only section 4.1 ("shorter sections are not designed here"). The skeleton now raises a TODO asking for section breaks.
- **ela-texts.csv** edition and rights: left for the lead. The field 10 TODO now asks the writer to give the basis where a row says "not stated" and to list that row under "For the lead".

## Social studies would also benefit, parked for its probe (data/plans/later.csv L28)

These fixes were gated off for social studies because they would change its output:

- `split_title` shapes
- earlier-grade and continuous use in `earlier_rows`
- retrieval junk (`retrieval_clauses`)
- the one-hop Respond and Check exclusion
- field 5 (kept evidence, reuse owner, coverage line, note printed once, parent pre-fill)
- one line per source-map row
- section length flag
- hook day
- begun codes
- `frame_models` wording
- school-days wording

## Gates

| Gate | Result |
|---|---|
| `unit_skeleton.py --self-test` | All passed, including 22 new cases on synthetic `--data-dir` and inline data |
| Social studies frozen diff | Identical, 138 files |
| `sequence.py check` and `frame.py check` on each touched course (science-kindergarten, science-grade-4, science-grade-7, english-language-arts-grade-11, geometry) | 0 failures |
| Overall `sequence.py check` | 0 failures |

Overall rule-2 notes went from 60 to 129. The new notes are all in math, ELA and science: earlier-grade rows that used to be hidden as "owned" now surface. Social studies notes are unchanged.

## Regenerated

All 37 courses from `--list science|ela|math` were regenerated with `--force` (259 unit files), including math-grade-4.

## Word counts, before and after

| Unit | Before | After |
|---|---|---|
| ELA K s04 | 27,004 | 16,269 |
| ELA 1 s01 | 26,389 | 16,039 |
| ELA 2 s01 | 21,831 | 13,525 |
| science 7 s04 | 6,984 | 5,022 |
| math 1 s03 | 6,871 | 4,973 |
| math 5 s04 | 3,750 | 2,645 |

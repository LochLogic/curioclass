# Science ladder: fixes after the report (2026-11-19)

Cory, after docs/reviews/ladder-science-report-2026-11-19.md: "Fix all that you can now, then let's pause. This
includes fixing what we found in this test, and outside of it." This is what was fixed, and what is left. Refine 1
and the climb past grade 3 wait for Cory.

## Gates and templates (outside the test)

- **plan.py.** Course-level days (unit C) are skipped by the consecutive-days check; one early opener day is a note,
  not a fail. A day that holds unit assessment (end) items needs no exit. Check-day part coverage is read across all
  of a unit's end items, on the unit's last check day. `phrase = none` in shows (a set-up goal piece) is a note.
- **lesson.py.** `unit: C` headers pass. The At home exit-ticket-last rule skips days holding end items. New
  `exit: half` header: a judged exit too long for a quarter page prints on a half sheet, two to a page. New gate:
  a page that teaches as new what the ledger records as review of a lower grade fails until it says "review". New
  note: a number in the section plan's `## Day N` block that the day and its items never use.
- **ledger.py.** `show` takes `--term` and `--course` filters (the whole ledger is too long to read in one piece);
  new `note` command corrects a row's note.
- **Docs and briefs.** LESSON-DAY.md and data/plans/README.md carry the rules above. plan-data.md gains step 5:
  rule 4 on the pieces, plan against data, sources, and an answer-key read before days are queued. write.md says to
  look terms up in the ledger, say review aloud, add ledger rows, and never bend a day to pass a gate.
- **K to grade 2 DEFAULTS.md.** At home minutes match the gate.
- Not added: an exit-reuse gate (word overlap flagged 242 of 440 exits; the answer-key cold read covers it).

## Content (the test)

Four fix agents, one a grade, then one for grade 3's long exits. Every FIRM finding in the samples is fixed, with
short SOFT findings and the known faults.

- **Kindergarten.** All 10 FIRM fixed; a new piece, u06-2/record-year-end.md; source B13 (prairie dog) added; the
  course-level days carry `unit: C`.
- **Grade 1.** All FIRM fixed (strips key now 11.8; otter and alligator captions reworded); review wording on the
  days the new gate named, ledger rows corrected for days 51 and 56; the u03-1 plan's day 25 exits match the data.
- **Grade 2.** All FIRM fixed; new items s02-X16b, s04-X40a/b, s05-X48b, s05-X53a (old X53 is now X53b); day 37 cut
  to task boxes read aloud; sources U14 and U15; day 10 on a half sheet; plan strip numbers match the data.
- **Grade 3.** All FIRM fixed (E1 asks about turns 3 and 5; E118k accepts Trial A only; X102 card; E90 and X111
  rewritten); days 101, 106 and 113 have exits; sources G56 to G61. Nine judged exits that did not fit now fit, six
  on half sheets; displaced parts became practice rows.

## Gates after

- plan.py: K to grade 3 have no failures except "section ... is not in data/units.csv" (a file on the blind list).
  Whole repository: no new failures; 58 removed.
- lesson.py: all 328 K to grade 3 days at 0 failures. Whole repository: 402 FAIL lines before, 291 after; the rest
  belong to courses still in planning.
- unitplan.py: PASS for all four courses. ledger.py check science: 5959 rows, 0 problems.

## Left for Cory

- **G51 (WMO World Weather Information Service).** Its rights are "paraphrase only" because the credit terms could
  not be read. Cory may want to check the terms, or leave it.
- **G61 (wood frogs).** Rests on a search summary of the page, not the page itself (the site refused reads).
- **Kindergarten template point.** The error-letter scheme clashes in one place; named by the K agent, left as is.
- Notes the gates print (plan numbers, set-up pieces) are readings, not failures.

Tokens: docs/reviews/ladder-science-tokens-2026-11-18.csv, five fix-after-report rows (about 996k in all).

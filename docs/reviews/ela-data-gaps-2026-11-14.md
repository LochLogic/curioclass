# ELA data gaps: texts and words (2026-11-14)

The ELA skeleton in `scripts/unit_skeleton.py` reports two kinds of missing data: the text records and the word
list. This review closes the text gap, sets a home for the word list and lists what still has to be found or
checked. Rights fields are left empty on purpose, since rights data is gathered later.

## Definitions used

`data/plans/README.md` (line 131) and `docs/courses/UNIT-PLAN.md` (the 2026-11-12 note) named `texts.csv`,
`questions.csv` and `words.csv` per course. Both said the columns would be fixed at the first pilot, and neither
defined them. The frames list what a text record holds: the measure, the qualitative headings, the reader and
task, the reason for its place, the rights, whole or excerpt, and the edition. The definition now sits in
UNIT-PLAN.md, in a section headed "ELA text and word data, defined 2026-11-14". In short:

- `data/plans/ela-texts.csv` is a single shared file with the columns course, unit, text_id, title, author,
  year, kind, form, length, use, part, edition, measure, demands, source, status, rights_basis, rights_checked,
  todo and note.
- It is shared instead of split per course because `plan.py check` fails on any `data/plans/<course>/` folder
  that has no `days.csv`, and no ELA course has days yet.
- A measure is recorded only when a free public number exists. The base text's module overviews supply two
  Lexile measures: grade 3 "Why the Frog Has a Long Tongue" at 670 and grade 4 "Fight to Survive!" at 890.
- The frames give "a reading level of about 1070" for Gatsby and "about 1340" for The Scarlet Letter, but they
  name no source for either number. Both texts are therefore marked "not on file", and the frames' numbers are
  kept in the note.

## File built

`data/plans/ela-texts.csv` has 385 rows. Each count is rows, then on file / to write / to choose / to confirm.

| Course | Rows | On file | To write | To choose | To confirm |
|---|---|---|---|---|---|
| kindergarten | 21 | 8 | 12 | 1 | 0 |
| grade 1 | 17 | 2 | 11 | 3 | 1 |
| grade 2 | 15 | 0 | 12 | 3 | 0 |
| grade 3 | 25 | 4 | 15 | 5 | 1 |
| grade 4 | 29 | 2 | 18 | 8 | 1 |
| grade 5 | 25 | 3 | 15 | 6 | 1 |
| grade 6 | 34 | 4 | 21 | 9 | 0 |
| grade 7 | 33 | 9 | 15 | 8 | 1 |
| grade 8 | 33 | 11 | 14 | 6 | 2 |
| grade 9 | 38 | 29 | 2 | 6 | 1 |
| grade 10 | 38 | 27 | 3 | 5 | 3 |
| grade 11 | 42 | 39 | 0 | 1 | 2 |
| grade 12 | 35 | 31 | 2 | 2 | 0 |

The K to 8 frames mostly describe Curio Class originals that are not written yet. Each of those has a row with
the frame's target band, so the unit plan writer can see what is owed. With `plan.py check` run after the build,
there were 0 failures.

## Texts not identified or not verified

- **Grade 1 "Birds are Human Helpers" (g1-u4-05).** The frame names it, but it is not in the text list of the
  grade 1 module 4 overview. It has to be found in the lesson materials.
- **Grade 5 rainforest-structure texts (g5-u2-04).** The grade 5 module 2 overview lists only "Bite at Night!".
  The texts on rainforest layers have to be found in the lesson materials.
- **Grade 3 and grade 4 base-text texts the frame does not name.** These are "More Than Anything Else: Context"
  (g3) and "Fight to Survive!" (g4). They are kept as to confirm.
- **Grade 3 frogs.** The frame says to use federal wildlife pages. The base text has its own CC BY texts on the
  same three frogs (Lexile 510 to 630), which are noted as a fallback.
- **Barnham, Tales of Nasr-ed-Din Khoja (1923), g8-u4-07.** A web search found no catalogue record. The fallback
  is Borrow, The Turkish Jester (1884).
- **Occom, "A Short Narrative of My Life" (g11-u3-11).** It was written in 1768 but first printed in 1982. A work
  first published between 1978 and 2002 can be protected until 2047. The frame treats it as public domain, so
  this needs a rights decision.
- **Twain, "The War Prayer".** The frame says it was printed in 1916. Its first printing was in 1923, in Europe
  and Elsewhere. It is still public domain, and the date is corrected in the row.
- **The UDHR (grade 5).** It is a UN document, not a US government work. The UN allows reuse, and this is
  recorded under rights later.
- **Other to-confirm rows:**
  - the Cotton Mather text on Onesimus
  - the parts of Wiley Bulletin 84
  - the version of "Barbara Allen"
  - the NHGRI and FDA cloning pages
  - a Pasteur translation for the 1864 Sorbonne lecture
  - the 1890 census table
- **"To choose" rows.** There are 76 of these, mostly federal agency pages and poem sets. They are named by kind
  until the unit plan picks them.

## The words.csv decision

The word list is unit plan output, not input data. APPROACH-ELA and the frames say it is drawn per unit from
that unit's texts. The writer should produce it as `data/plans/<course>/wordlist.csv`, with the columns unit,
word, text_id, week and when. The name is not `words.csv` because `plan.py` (line 659) already reads `words.csv`
per course as settled word rules (pattern, use, reason). An ELA word list under that name would break the
reader.

## Changes needed (not made: outside this task's ownership)

**`scripts/unit_skeleton.py`, ELA branch of `field2_extras`:**

1. The "Text set (frame, C3 column)" line reads `fr[5]`, but only grades 6 to 8 keep texts in that column. For
   K to 5 and 9 to 12 it prints "Not used (ELA)" or "None (ELA)". Replace it with the rows of
   `ela-texts.csv` for this course and unit, one line per text with the fields title, author, year, use, part
   and status.
2. Replace the "Anchor and paired texts ... Missing data: the text records (texts.csv, UNIT-PLAN.md) are not
   built." line with a request to the writer. The writer confirms each anchor and paired row, fills `to choose`
   and `to confirm` rows, and notes any text added or dropped. If no rows exist for the unit, report "no rows in
   data/plans/ela-texts.csv".
3. Change the "Text complexity ... (missing data: texts.csv)" line so it prints each anchor's `measure` and
   `demands` from the file, and asks the writer only for the support.
4. Change the "Word list ... (missing data: words.csv is not built)" line to: "Word list: draw about 8 to 10
   words a week from this unit's texts and write them to data/plans/<course>/wordlist.csv (unit, word,
   text_id, week, when)". This is a writer task, not missing data.
5. In the sources line (about line 987), take each author and edition from the same rows. The rights line stays
   "rights: TODO" until the rights columns are filled.

**`scripts/unitplan.py` (optional, after line 258):** for an ELA plan, warn when an anchor row of the unit in
`ela-texts.csv` is not named in field 2 or field 10.

**`scripts/plan.py`:**

- Keep reading `words.csv` as word rules.
- Before ELA course folders are made, either let `courses()` skip a folder with no `days.csv`, or move
  `ela-texts.csv` rows into each folder only once that course has days.

**Wording to update (owned by others):**

- `data/plans/README.md` line 131 still names `texts.csv` and `words.csv` per course.
- The frames' "data/plans/<course>/texts.csv" wording should point to `data/plans/ela-texts.csv` until the split.

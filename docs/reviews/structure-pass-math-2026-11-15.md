# Structure pass, math group, 2026-11-15

Applies the "For the structure pass" items of the 37 scope fix reports (docs/reviews/sequence-<course>-fixes-2026-11-15.md)
whose target file the math group owns: data/progressions/math.csv, docs/RUBRIC-MATH-K8.md, docs/RUBRIC-MATH-HS.md,
docs/APPROACH-MATH.md, docs/APPROACH-SOURCES.md, data/coverage.csv, data/modules.csv, data/plans/later.csv,
scripts/frame.py, and the math heading of docs/reviews/DIGEST.md.

## Applied

- **data/progressions/math.csv** (CRLF and quoting kept; round trip verified):
  - Algebra I 1, 2: alg1-center-spread and alg1-rearrange-formulas assume m8-roots; m8-roots hands on to both (the gate
    needs both ends of a handoff).
  - Algebra II 1, 2: the "Skips grade 10 on purpose" sentence and the "Re-entry (recall required): open with a short
    readiness check on" prefix replaced in 21 grade-11 rows; the 22nd row, alg2-quadratics-complex-solutions, takes
    Geometry's specific wording (see Conflicts).
  - Algebra II 3: alg2-rational-exponents assumes m8-integer-exponents; m8-integer-exponents hands on to it.
  - Algebra II 4: alg2-experiments-significance health teacher note.
  - Geometry 1: eleven note replacements (geo-parallelogram-proofs to alg2-quadratics-complex-solutions, plus its
    skip sentence).
  - Grade 4 1, 2 (m4-decimal-notation, m4-measurement-problems); grade 5 1 (m5-expressions); grade 6 1 (m6-gcf-lcm);
    grade 8 1 to 3 (m8-integer-exponents, m8-roots, m8-coordinate-distance).
- **scripts/frame.py**: contribution note now searches the whole unit row (`' '.join(u.values())`) and reads "name each
  begun code in What students learn, with its later owner (no ~CODE in Owned standards)"; docstring bullet updated;
  PINS science-grade-2 `{40: 84}` to `{58: 98}` (science grade 2 item 2).
- **docs/RUBRIC-MATH-K8.md**: Gateway 3 teacher-support cell now says readiness checks or retrieval tasks placed by
  sequence-write.md rule 2, with the grade-number rule spelled out (grades 2, 3, 5, 6 merged); Geometry's "High school
  planning note" appended, pointing to RUBRIC-MATH-HS and later.csv L25.
- **docs/APPROACH-MATH.md**: grade 4 reteach sentence (grade 4 item 3).
- **docs/APPROACH-SOURCES.md**: two math table rows (grade 8 item 5); high school science evidence guide and three
  HS evidence statements in the section 3 table (Chemistry 12, Biology 5, one row for the guide with both URLs); grade
  4 lesson 5.14 pointer after the IM K-5 lesson-page bullet; new section "Science and ELA scope and sequence reads,
  2026-11-15" with the ELA grade 10 access note (item 8) and the two science grade 2 sources (item 8).
- **data/modules.csv**: math-6-dependent-and-independent-variables standards `6.EE.C.9`, frameworks `CCSS-Math`.
- **data/coverage.csv**: removed the math grade 6 NSPFE.Earning Income row (grade 6 item 4).
- **data/plans/later.csv**: L25 detail rewritten (Algebra I item 4, merged with Algebra II item 6's content list).
- **docs/reviews/DIGEST.md**: "## Scope fix pass, 2026-11-15: math" appended, 21 lines.

## Skipped

- RUBRIC-MATH-HS.md not created (Algebra II item 6): no report gives its content; listed in later.csv L25.
- data/modules/math.txt line 71 (grade 6 item 2): not a math-group file. The lead must drop `;NSPFE.Earning Income`
  there, or the next build_db.py run puts it back into modules.csv.
- frame.py items from science grade 1 and the ELA/science "regenerate the calendar" items: they ask for `frame.py sync`,
  which the lead runs. Split unit runs (science grade 1's unit 8 fall run) are already handled by the calendar code.
- All other items target files outside this group.

## Conflicts reconciled

- frame.py: six reports gave `' '.join(u.values())`, grade 1 gave Owned standards plus What students learn; took the
  majority (wider) test. Seven message wordings; wrote one that carries all of them.
- alg2-quadratics-complex-solutions: Geometry's specific text (retrieve completing the square, taught days 111 and 125;
  readiness only for the quadratic formula) instead of Algebra II's generic ledger sentence, per lead math call 5.
  Prefix written "Re-entry:" to match the other grade-11 rows.
- Geometry's new retrieval wordings lost the row ids, which raised eight progression "skips a grade, say why" notes;
  added the ids in brackets (lead math call 4), notes back to zero.
- RUBRIC-MATH-K8: Geometry's high school note applied; L25 now says K8 holds only that planning note, no criteria.

## For Cory

None.

## Gates

- progression.py check math: 305 rows, 0 failures, no handoff notes.
- frame.py check (all frames): exit 0, 0 failures. Contribution notes left: one, math-grade-7 unit 3 (7.RP.A.2a not
  named in the unit row; the math-grade-7 frame owner should name it).
- sequence.py check, all 12 math courses: 0 failures.
- plan.py check: exit 0.
- frame.py has no self-test.

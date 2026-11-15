# Structure pass, ELA group, 2026-11-15

Applied the "For the structure pass" items of the thirteen ELA fix reports whose target file the ELA group owns. The
scratchpad extract missed the grade 6 and grade 9 items; both were applied from the reports themselves.

## Applied

- **data/plans/ela-texts.csv** (394 rows, was 385): grade 1 (g1-u1-04, both poem rows, g1-u4-01 form, g1-u4-05,
  g1-u2-03 note, the three todo rewrites); grade 2 (three original-poem rows, g2-u3-02 anchor, both fable sources);
  grade 3 (g3-u1-06, g3-u3-04, g3-u4-02 anchors); grade 4 (five poem notes, g4-u3-02 edition, g4-u2-05 note); grade 5
  (g5-u1-02 anchor, three count-once notes); grade 6 (g6-u2-05 anchor and demands, g6-u3-01 length, part, note);
  grade 7 (g7-u2-01, g7-u6-01 lengths and notes with source URLs); grade 9 (ten edition/length/note cells, seven
  independent-offer rows g9-u2-05 to g9-u8-08, editions from the library source catalogue); grade 10 (new g10-u3-07,
  g10-u3-04 chapters 1 to 4, g10-u1-01 edition, status to confirm, todo); grade 11 (g11-u3-02 paired, new g11-u7-09,
  six length cells, g11-u8-01 and g11-u8-02 exact selections); grade 12 (seven use swaps, three title/length pairs,
  Harlem cluster note); kindergarten (seven course-record notes).
- **data/progressions/ela.csv**: e1-short-vowels, e1-long-vowels, e2-vowel-teams; the word-part list across
  e3-long-words, e4-long-words, e4-word-strategies, e5-long-words, e6/e7/e8-word-strategies; e5-reading-range,
  e5-writing-tasks, e5-fluency; e7-word-choice-info, e7-argument-writing, e7-narrative-writing; e8-myth-made-new; the
  word-family list across e9/e10/e11/e12 word-strategies; e10-l-syntax-style; e11-routine-writing, e11-lit-themes,
  e11-lit-irony; e12-info-ideas-events, e12-info-founding-documents, e12-research, e12-academic-words,
  e12-presentation.
- **docs/RUBRIC-ELA.md**: pilot phrase (line 5), grade 6 intro paragraph, the three grades 3 to 5 Gateway 1 cells,
  seven grade 6 Gateway 2 evidence cells.
- **data/plans/us-history-i/days.csv**: day 71 goal (draft feedback; score from the single final artifact on ELA day
  75); days 56, 61, 66 notes relabelled as progress checkpoints toward ELA days 60, 65, 70.
- **docs/reviews/DIGEST.md**: "Scope fix pass, 2026-11-15: ELA" heading appended.

## The lists (lead call ELA 4)

Grades 3 to 8, one word-part list, each part new in one grade: grade 3 affixes (pre-, mis-, -ful, -less, -ness, -ly,
-ment; un-, re-, dis-, -able, -tion, -sion, -ous retrieved); grade 4 scrib/script, tract, graph, photo, tele, port,
rupt, ject, aud, vis, struct, form; grade 5 dict, spect, bio, geo, meter, therm, mit/miss, cred, aqua/hydro, -ity,
-ian, -ial, -ive, -ance, inter-, trans-, multi-; grade 6 phon, gram, glyph (graph, scrib/script, aud retrieved);
grade 7 immun, epi, pan, demos, logy; grade 8 tox, pharm, serv, ced/cede, ad-. No duplicates among the fixers' lists.

Grades 9 to 12, one word-family list, each root new in one grade: grade 9 analyze, derive, infer, constitute, vary,
synthesize; grade 10 create, perceive (cap/cept), reproduce, persuade, plus transform built from retrieved form and
trans-; grade 11 compel, sustain, legislate, hypothesize (hypo- new, thes/thet retrieved); grade 12 reflect, discern,
exclude, deliberate, justify, qualify. Duplicates resolved to the earlier grade (see For the lead).

## Conflicts reconciled

- RUBRIC-ELA Gateway 1 cells: grades 3 and 5 both replaced the same three cells; merged into one cell per row naming
  each grade, with "no evidence entry filed" for grade 4. The fluency cell keeps its grade 6 parenthetical.
- g11-u7-09: `source` set to `public domain` (the column's convention) and the local path moved to `note`; edition
  marked proposed.
- g11-u8-01/02: the report gave selections, not cell values; recorded as title, length, edition or note.
- us-history-i day 71: "day 75" written as "ELA day 75" (history day 75 is a different lesson); day 70's goal said the
  paper is "scored day 71" and now points to the same final artifact.

## Skipped

- data/library/sources.csv shelley-frank pg 84 to 41445: the 41445 source is not in library/_sources, so
  library_check would lose Frankenstein's text (a new gate failure), and library_process joins every listed pg
  number. Fetch 41445 first (a download), then change pg and restore library/frankenstein/text.md.
- Kindergarten scope and sequence: the `#course-text-record` anchor already exists (heading "Course text record").
- Items in files outside this group: library/frankenstein, douglass-narrative, scarlet-letter text.md and story.json;
  docs/APPROACH-SOURCES.md; civics frame line 186; docs/pipeline/briefs/frame-write.md (grade 8 items 3 and 4).

## For the lead

- Grade 10 teaches synthesize/synthesis/synthetic as new in weeks 23 to 31 (days 111, 116, 121, 128, 137, 141, 146,
  151); grade 9 owns it (days 126, 142, 147, 151, 159). Grade 10 needs a new family or a retrieval label there.
- Grade 10 transform (days 46 to 81) has no new root (form grade 4, trans- grade 5); label only, or swap.
- Grade 11 persuade (days 51, 56, 61, 66, 71) is grade 10's family (days 89 to 106); conceive (days 8, 11, 17, 22)
  reuses grade 10's cap/cept; hypothesize (days 126 to 159) reuses grade 9's thes/thet. Grade 11 scope line 167
  claims cap/cept is distinct from grade 10, and day 4 calls grade 9's families "grade 10's".
- docs/courses/us-history-i/s04.md line 96 still says the reform paper is "scored day 71".

## For Cory

Grade 12 audience: a one-child, one-parent home has no second listener, and internal ELA panels do not supply
paired history's beyond-classroom audience.

## Gates

progression.py check ela 0 failures; sequence.py check, all 13 ELA courses and us-history-i, 0 failures; frame.py
check us-history-i 0 failures; plan.py check exit 0; library_check unchanged (12 existing problems).

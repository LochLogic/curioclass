# Expert read: ELA progression (2026-11-13)

A cold read of the English language arts progression, K to 12, by the curriculum expert (docs/agents/EXPERT.md,
lens docs/agents/lenses/ela.md, bar docs/RUBRIC-ELA.md). No course page under docs/courses/ and no earlier
review of an ELA course was opened. The reconcile report was read last, only to see what it changed.

## What I read

- data/progressions/ela.csv: 374 rows (K 29, 1 31, 2 30, 3 28, 4 30, 5 30, 6 29, 7 28, 8 29, 9 24, 10 26,
  11 30, 12 30), every column of every row; the notes in full for all foundational rows, every reading-range row,
  every discussion, seminar and research row, and the 9/10 and 11/12 twin rows that a finding rests on; the rest by
  their standard, assumes, hands_on, model and words columns, with notes opened where a check needed them.
- data/progressions/ela-excluded.csv: header only, no code excluded.
- data/progressions/parts/ela-k2-edges.md (the K to 2 handoff list).
- data/standards/ccss-ela-standards-full.txt (868 lines) and data/standards/c3-indicators.txt (codes).
- data/progressions/social-studies.csv and science.csv, only to place each `cross_subject` lean in its grade.
- docs/reviews/progression-ela-stitch-2026-11-13.md, then, last, progression-ela-reconcile-2026-11-13.md.
- For REPEAT tags: docs/reviews/progression-science-2026-11-13.md and progression-social-studies-2026-11-13.md.
- Gate: `python -X utf8 scripts/plan.py check` gives "progression ela: 374 rows, 0 failure(s)";
  `scripts/progression.py check ela` adds one note (e8-dramatic-irony to e11-lit-irony skips two grades), and
  both rows already say why. Coverage of every anchor standard, single-grade ownership, both ends of every
  handoff, model order and cross_subject codes are settled by the gate and were not re-counted.

Scripts I ran on the data (kept in the scratchpad, not the repo) checked: lettered sub-parts named nowhere and
whose parent is named nowhere (none); rows with no assumes above K or no hands_on below 12 (none); every
cross_subject lean against the grade that owns it in the other subject; each standard thread (RL.x.7, L.x.3 and
so on) against the assumes of the next grade's owner; the first grade each key word appears in `words`
against its first use in notes; and strand counts by grade.

## Verdict

The progression is sound and unusually well written: every row says what changed from the grade before and
where its limit sits, the K to 2 phonics follows a planned order with decodable texts bound to taught patterns,
grades 3 to 5 carry a real long-word and fluency sequence, and the 9-10 and 11-12 bands climb inside the band.
The biggest risk is small and local: two K to 3 rows disagree on when Greek and Latin roots start, and grade 3
lists as new three suffixes grade 2 already decoded, which a grade 3 writer would build days from. Most of the
rest is wiring (five missing standard-thread links, one forward cross-subject lean) and the 11-12 discussion
rows falling to once a unit. Seven findings, none moves a standard.

## Findings, most serious first

### 1. Roots start in two different grades, and grade 3 relists grade 2 suffixes as new (moderate; firm)

- **Skill ids:** e2-prefixes-suffixes, e3-long-words, e3-word-strategies, e4-long-words, e4-word-strategies.
- **What is wrong:** e2-prefixes-suffixes ends "Latin and Greek roots begin in grade 3". e3-word-strategies says
  "Greek and Latin roots are grade 4 (L.4.4b)" and e4-long-words says grade 4 brings "the first Greek and Latin
  roots". The standards agree with grades 3 and 4: L.3.4c is a known English root (company, companion), L.4.4b
  names Greek and Latin roots. Second, e2-prefixes-suffixes decodes -tion, -sion, -able and -ible, and
  e2-two-syllable-words adds -ous; e3-long-words then lists -tion, -sion and -ous as grade 3's "common Latin
  suffixes (3b)" with no word that grade 2 met them.
- **Why it matters:** a grade 3 phonics writer reads the grade 2 boundary as a promise and may add Greek and Latin
  roots a year early, or spend the RF.3.3b weeks teaching suffixes as new that students decoded last year,
  instead of moving them onto new and longer bases and adding their meaning.
- **Fix (row edits):** e2-prefixes-suffixes notes, last sentence, to: "Boundary: one prefix or suffix on a known
  base word; known English roots are grade 3 (L.3.4c) and Greek and Latin roots grade 4 (L.4.4b)." e3-long-words
  notes, after "(3b)": "Grade 2 decoded -tion, -sion, -able and -ous on known base words; grade 3 reviews them,
  adds -ment and their meanings, and reads them on new and longer bases."
- **LAYER:** progression. **REPEAT:** yes (stale or crossed notes, as in the science and social studies reads).

### 2. Five standard threads with no assumes link from the grade before (moderate; firm)

Each row below owns the next grade's version of a standard whose earlier version sits on a row it does not
assume. The gate cannot see this: it checks that links agree at both ends, not that the real prerequisite is
linked.

| Standard thread | Earlier row (owns) | Later row (owns) | Why it is the real prerequisite |
|---|---|---|---|
| SL.3.5 to SL.4.5 | e3-fluency (SL.3.5, audio recordings) | e4-presenting (SL.4.5) | grade 4 adds audio and visuals to the recordings grade 3 made |
| L.4.3 to L.5.3 | e4-formal-informal (L.4.3, words and punctuation for effect) | e5-grammar (L.5.3a, expand, combine, reduce for style) | the knowledge-of-language strand climbs from one to the other |
| SL.7.2 to SL.8.2 | e7-central-ideas-develop (SL.7.2, main ideas in diverse media) | e8-medium-choice (SL.8.2, purpose and motive of media) | grade 8 judges motive in the same media grade 7 analysed |
| L.8.6 to L.9-10.6 | e8-word-choice-info (L.8.6, academic and domain words) | e9-l-word-strategies (~L.9-10.6) | the academic word list carries on |
| L.9-10.3 in grade 9 to grade 10 | e9-w-short-research (~L.9-10.3, style manual) | e10-l-syntax-style (owns L.9-10.3) | the owner of the band standard does not assume the row that started it |

- **Why it matters:** a section writer works from `assumes` to plan the warm-up and the "what they know" note; a
  missing link means the earlier skill is not reactivated, and the reading pack for the later unit leaves it out.
- **Fix:** add each later row to the earlier row's `hands_on` and the earlier row to the later row's `assumes`
  (five pairs, as in the table). No note changes; each later row's note already describes the climb.
- Not raised, on purpose: RI.6.7 to RI.7.7, L.6.1 to L.7.1, RI.5 and RI.6 in K to 4, RL.5 grade 1 to 2. The
  standard's content changes there, and each later row already assumes the right skill.
- **LAYER:** progression. **REPEAT:** yes (social studies finding 2 and 3, science finding 5).

### 3. Formal discussion falls to once a unit in grades 11 and 12, and is never paced in K to 2 (moderate; likely)

- **Skill ids:** e11-seminar, e12-seminar, ek-discussion, e1-discussion, e2-discussion.
- **What is wrong:** grades 3 to 5 plan at least two formal text discussions a unit, grades 6 to 8 one every two
  weeks, grades 9 and 10 at least twice a unit. e11-seminar drops to "a seminar each unit", and e12-seminar
  states no frequency. The three K to 2 rows name routines but no frequency.
- **Why it matters:** the bar scores discussion as "often" (RUBRIC-ELA, 2j), and the lens lists "discussion is
  formal too rarely to be often" as a scope and sequence error. A frame writer copying the row will plan four or
  five discussions in the year in grade 11, fewer than grade 3.
- **Fix:** e11-seminar notes: "Practised in a seminar each unit" becomes "Practised at least twice a unit: one
  full seminar and one shorter text discussion". e12-seminar: add "At least twice a unit, one a full
  student-led seminar." ek-, e1- and e2-discussion: add "A named protocol on the module text most days, at least
  two a week, as the base text runs them."
- **LAYER:** progression. **REPEAT:** new.

### 4. A grade 6 row leans on a grade 8 social studies skill (minor; firm)

- **Skill id:** e6-argument-writing, `cross_subject` = social-studies:D4.1.6-8.
- **What is wrong:** in data/progressions/social-studies.csv, D4.1.6-8 is owned only by ss8-court-research
  (grade 8). The brief's rule is a lean on a skill the other subject owns at or before the grade. The reconcile
  report added this lean (its difference 10, from the old grade 6 module); this read disagrees with that pick.
- **Why it matters:** the grade 6 writer would point students at an argument routine their social studies course
  has not taught yet.
- **Fix:** replace with `social-studies:ss6-hammurabi-code (an argument about the past built from a source,
  D2.His.16.6-8)`. That grade 6 row names D2.His.16.6-8 (organise evidence into an argument about the past) and
  reads the Code of Hammurabi as a source, so the lean is real and same-grade.
- **LAYER:** progression. **REPEAT:** yes (social studies finding 7).

### 5. Teacher terms in the students' word lists (minor; firm)

- **Skill ids and words:** ek-emergent-reader "decodable"; e3-reading-range "band"; e4-reading-range "band";
  e5-reading-range "band", "high end"; e8-reading-range "high end".
- **What is wrong:** the `words` column is the key words a row teaches at the grade's reading level. These are
  words of the plan (text complexity bands, decodable texts), not words a five- or eight-year-old is taught.
- **Fix:** drop them from those five rows. Keep "stamina", "fluency" and "multisyllabic" in grades 3 and up, which
  students can use about their own reading.
- Words otherwise check out: every key literary and rhetorical term (claim, theme, central idea, connotation,
  dramatic irony, counterclaim, rhetoric) is in a `words` list no later than the grade that teaches it; the earlier
  hits in notes are boundary sentences ("counterclaims are not in K to 5"), not uses.
- **LAYER:** progression. **REPEAT:** yes (science finding 11, social studies finding 11).

### 6. A grade 10 lean on a statistics standard most courses teach later (minor; likely)

- **Skill id:** e10-ri-argument-evaluate, `cross_subject` = math:S-IC.B.6 (evaluating reports based on data).
- **What is wrong:** S-IC (making inferences and justifying conclusions) usually sits in Algebra 2 or a statistics
  course, grade 11 or later, in the common high school sequences (from memory). S-ID.C.9 for grade 9 and S-ID.B.5
  for grade 11 are fine in any common sequence.
- **Fix:** keep it for now, and check it against data/progressions/math.csv when that file lands (it was not
  mine to read on this run). If S-IC.B.6 is owned after grade 10 there, change the lean to
  `math:8.SP.A.1 (patterns of association in data)`, which e10-ri-mediums already uses.
- **LAYER:** progression. **REPEAT:** new.

### 7. The 9 to 12 long-text shelf is one tradition and mostly one century (moderate; judgment call)

- **Skill ids:** e9-rl-range-scaffolded, e10-rl-range-independent, e11-reading-band, e12-reading-band (and the
  rows that read their texts).
- **What is wrong:** the whole long texts across four years are Romeo and Juliet, the Odyssey in parts,
  Frankenstein, Julius Caesar, The Scarlet Letter, Douglass's Narrative, Hamlet, The Great Gatsby and Pride and
  Prejudice. Short sets do reach wider (Tagore, Chekhov, Chief Joseph, Du Bois, Woolf, a world literature set
  from three regions in grade 10), but every book read whole is British, American or Greek, and all but Gatsby
  are before 1900. BASELINE rule 29 (newer, relatable texts, mostly original) binds only K to 8, so this is
  allowed; the cause is plain: public domain.
- **Why it matters:** the bar reports the range of people in and behind the texts (2e) and the lens names "the
  year's texts lean to one era, one tradition" as a course frame error. A reviewer would say so in all four
  years. The stitch flagged world literature as thin (its item 14), not the long-text shelf as a whole.
- **Fix:** a question for Cory (below). Inside the rows, nothing changes now; the course frames are where a
  long original or recent text would go.
- **LAYER:** base text. **REPEAT:** yes (RUBRIC-ELA records the same "one era and one tradition" gap for the
  grade 6 shelf).

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| e2-prefixes-suffixes boundary: English roots grade 3, Greek and Latin roots grade 4 | L.3.4c and L.4.4b say so; two rows disagreed | data/progressions/ela.csv |
| e3-long-words names the grade 2 suffixes as review and adds -ment and meaning | grade 2 rows already decode -tion, -sion, -able, -ous | data/progressions/ela.csv |
| Five assumes and hands_on pairs added (finding 2 table) | each is the same standard's earlier version | data/progressions/ela.csv |
| e11-seminar and e12-seminar at least twice a unit; K to 2 discussion rows at least two named protocols a week | match grades 3 to 10 and the "often" bar | data/progressions/ela.csv |
| e6-argument-writing cross_subject to social-studies:ss6-hammurabi-code | D4.1.6-8 is owned in grade 8; overrides reconcile difference 10 | data/progressions/ela.csv |
| Drop "decodable", "band" and "high end" from five `words` cells | plan words, not student words | data/progressions/ela.csv |
| e10-ri-argument-evaluate math lean held until math.csv is read | cannot place S-IC.B.6 yet | none now |

## For Cory

- **Grades 9 to 12 long texts (audience, scope):** every book read whole is British, American or Greek, and all
  but one before 1900, because they are free to use. Should grades 9 to 12 also carry one long original or recent
  text a year (as BASELINE rule 29 does for K to 8), or stay with the public-domain shelf and widen only the short
  sets? Pick: one long text a year that is original or recent public domain from outside the British and American
  tradition, placed by each course frame.

## Lens checklist: progression layer

| Line | Mark |
|---|---|
| A reading or writing skill climbs nowhere (same task, same text demand in two grades) | Met. Every row states the change from the grade before; the 9/10 and 11/12 twin rows name different texts and a different demand (one theme then two in tension; teacher-named ideas then found alone; teacher roles then student-led) |
| K to 2: a phonics element used in decodable text before the grade that teaches it, or a pattern never taught | Met. Decodables are bound to taught patterns in every K to 2 foundational row; r-controlled vowels come in grade 1 ahead of RF.2 on purpose and are reviewed in grade 2 |
| Grade 3 assumes foundational skills grade 2 does not finish, with no grade 3 phonics and fluency plan | Met, with finding 1: e3-long-words and e3-fluency are a real plan; the overlap with grade 2 suffixes needs naming |
| Topic sets do not connect across grades, or repeat the same topic at the same depth | Met as far as rows show: K to 5 science topics differ each year (trees, birds, pollinators, frogs, animal defenses, ecosystems) and climb; the leaning is to life science. The full test is a course frame read |
| The writing types are not balanced across the grades | Met: 30/35/35 in grades 3 to 5, two pieces of each type a year in 6 to 8, 40/40/20 in 9 to 12 |
| Discussion formal too rarely to be "often" (scope and sequence line, read here because rows set it) | Missed in grades 11 and 12, unpaced in K to 2 (finding 3) |
| Research appears once or never | Met: one to three projects a year in every grade, growing from shared research to self-generated questions |
| The year's texts lean to one era or one tradition (course frame line, visible in row notes) | Missed for the 9 to 12 long texts (finding 7) |
| Other course frame, unit and day lines | Not applicable at this layer |

## Pace through the grades

Rows by grade run 24 to 31. Grade 9 (24) and 10 (26) are lowest because band rows merge two or three standards;
that is row grain, not load. By strand: foundational K 8, 1 9, 2 6, 3 to 5 two each, then none (RF ends at 5, as
the standards do); language 3 a grade, 5 in grades 11 and 12; reading informational 3 in K (K shares its RI rows
with RL) then 5 to 8; reading literature 6 to 9; writing 5 to 7; speaking and listening 2 to 3. No strand stops
and starts again. No finding.

## What is right and should not be touched

- The rule that words are read, never guessed from a picture or context, is stated on every foundational row and
  on every row that uses context (RF.x.4c is a check after decoding).
- The complexity bands on the reading-range rows match the 2012 supplement's measures (420 to 820, 740 to 1010,
  925 to 1185, 1050 to 1335, 1185 to 1385), and support is withdrawn on the standards' own pattern: scaffolding at
  the high end in the first year of a band, independent by its end.
- The band design for 9 to 12 (practised with `~` in the first year, owned in the second) keeps one owner per
  standard and still gives each year a distinct demand.
- Grade 6 keeps a weekly fluency reread and an oral reading check with the teacher holding the watch.
- Teacher notes on sensitive texts ('The War Prayer', advertisements written for the course, outdoor bee
  observation) are where they are needed.
- The e8-dramatic-irony to e11-lit-irony skip is explained in both rows; leave it.

## What I could not judge

- Whether the K to 2 letter and pattern order matches EL Education's Skills Block cycle by cycle: the base text
  was not opened on this run, so the order rests on the rows' own claims.
- Whether Gateway 1 for grades 3 to 5 is satisfied by two foundational rows a grade: that depends on the scope
  and sequence, and the 3-5 evidence guide's Gateway 1 lists were not reopened.
- The math leans, until data/progressions/math.csv exists (finding 6).

## Sources

- Common Core State Standards for ELA (data/standards/ccss-ela-standards-full.txt): ownership, sub-parts, and the
  L.3.4c and L.4.4b wording behind finding 1.
- C3 Framework codes (data/standards/c3-indicators.txt) and data/progressions/social-studies.csv: finding 4.
- Common Core Appendix A supplement (2012) band measures: from memory, matched against the rows' figures.
- EdReports ELA criteria as summarised in docs/RUBRIC-ELA.md (2e, 2j): findings 3 and 7.
- No outside source was fetched on this run; firm findings rest on the standards text and the repo's own data.

## For the source list

Nothing new.

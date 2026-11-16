# Probe 2 measure 2: unit plans changed, social studies (2026-11-15)

Read-only job for docs/pipeline/PROBE-GUARD.md measure 2, second social studies probe. Method as in
docs/reviews/probe-measure2-2026-11-15.md: scripts over the unit plan files (docs/courses/<course>/sNN.md, field 5, 6,
7, 10 and the day list), then a read of every hit. Not a full re-read. Denominator: 137 unit plans (15 social studies
courses, 138 units, less world-history-i unit 3, which was fixed).

Faults looked for, from the fixes in world-history-i s03 (commit 71d2d18d, defects.csv rows 2026-11-15 s03):
F1 feedback and revision inside the period the work was made. F2 a wrong answer filed under a letter whose text does
not describe it. F3 one wrong answer or exit tagged with two letters ("D or I"). F4 a planned quotation from a text with
no free checkable English translation. F5 an end item built on our own summary of a source (or on a source not read),
where a checked passage was needed. F6 (new rule, not a fault) no component-to-move table in field 7.

## 1. Result

| Fault | Units | What was counted |
|---|---|---|
| F1 | 21 | same-day feedback and revision |
| F2 | 5 | wrong answer under a letter that does not describe it |
| F3 | 12 | "or" tag on one wrong answer (or on one exit) |
| F4 | 3 | quotation planned without a free checkable English text |
| F5 | 34 | summary or paraphrase of a free or unread source as the end item stimulus (grades 6 to 12) |
| Any of F1 to F5 | **57 of 137 (42%)** | union, units counted once |

Band by measure 2 (on: the probed unit only, or 10% or fewer; off: more than 25%): **Off**. With F5 left out (the
fault least sure to be one in every unit, see section 4), the union is 33 of 137 (24%), which is Watch at the edge of
Off. F1 alone (21, 15%) is Watch.

F6: **137 of 137 units lack the component-to-move table in field 7** (no unit but world-history-i s03 has a
Component and move table anywhere). It is a new rule, so it is a rebuild list, not a fault count, and is not in the 57.

## 2. By course (units with each fault)

Units per course in brackets, world-history-i without unit 3.

| Course | Units | F1 | F2 | F3 | F4 | F5 | Any |
|---|---|---|---|---|---|---|---|
| social-studies-kindergarten | 6 | | | | | | 0 |
| social-studies-grade-1 | 8 | s01 | | | | | 1 |
| social-studies-grade-2 | 7 | | | s01 to s07 | | | 7 |
| social-studies-grade-3 | 7 | s03, s05, s06 | s04 | | | | 4 |
| social-studies-grade-4 | 7 | | | | | | 0 |
| social-studies-grade-5 | 10 | | s07 | | | | 1 |
| civics-government-and-civic-life | 10 | | | | | s01, s02, s03, s08 | 4 |
| economics | 9 | | | | | s03, s05, s06, s07, s08, s09 | 6 |
| us-government-and-politics | 9 | s05, s07 | | s03 | | | 3 |
| us-history-i | 9 | | s05 | | | s06, s08 | 3 |
| us-history-ii | 12 | | | | | | 0 |
| world-geography-and-ancient-civilizations-i | 11 | | | s10, s11 | s05 | s07, s09, s10 | 5 |
| world-geography-and-ancient-civilizations-ii | 12 | | | | | s07, s08, s09, s11, s12 | 5 |
| world-history-i | 9 | s01, s02, s04, s06, s07 | | s04, s07 | s08 | s01, s06, s07, s08, s09, s10 | 8 |
| world-history-ii | 11 | s01 to s10 | s01, s03 | | s01 | s01 to s08 | 10 |
| **Total** | **137** | **21** | **5** | **12** | **3** | **34** | **57** |

## 3. Evidence, one line per unit

### F1 (feedback and revision in the period the work was made)
- grade-1 s01 day 8: "15 minutes practice, 2 written picture feedback on rule and duty, 3 retry."
- grade-3 s03 day 66, s05 day 119, s06 day 134: a fresh attempt, then "teacher written check" or "teacher written feedback
  and independent ... revision" in the same period (for example s03: "fresh savings attempt 5, teacher written check 5,
  independent savings revision 10").
- us-government-and-politics s05 day 42: the presentation is made and scored that day; "Written feedback ... precedes
  revision within the existing fifteen-minute revision and conference block." s07 day 61: the argument is written and
  scored that day; "return a written criterion note on the argument and allow revision before collection."
- world-history-i s01 day 13 ("closing claim receives five minutes written feedback and five revision within thirty
  writing minutes"), s02 day 28 ("final map and claim twenty, written check five, revision five"), s04 day 61 ("claim
  draft twenty-five, written feedback five, revision five"), s06 day 87 ("claim twenty, written feedback five, revision
  ten"), s07 day 107 ("draft twenty-five, written feedback five, revision five"). Same pattern as s03 day 44 before the fix.
- world-history-ii s01 d13, s02 d24, s03 d37, s04 d56, s05 d67, s06 d86, s07 d105, s08 d119, s09 d131, s10 d142: each
  reads "new [work] N, written peer criterion feedback N, revision N" inside product or argument time, then "score
  revised work." Ten of eleven units; s11 returns teacher feedback before day 151 and is clear.
- Not counted: days that return feedback on earlier work and revise it (grade 3 and 4 respond days, us-history-i s05 d81,
  s09 d150), and "collected for feedback and later revision" rows in us-history-ii.

### F2 (wrong answer under a letter that does not describe it)
Found by word overlap of each tagged wrong answer with its letter's register text (184 zero-overlap rows), then read.
- grade-3 s04: "All place names were given by settlers" filed under G, "Contributions belong to all nations interchangeably."
- grade-5 s07: "Nobody ever petitioned before the internet" under G, "One hero or method ended injustice."
- us-history-i s05: "interchangeable offices" under D, "Lee was Confederate president."
- world-history-ii s01: "every territory became an independent modern nation state" under B, "European monarchs all held unlimited power."
- world-history-ii s03: "repeat the original answer without evidence" under I, "A source's perspective makes it wholly true or wholly useless"; "Colonized people had no knowledge of their own past" under G, "Western culture owed nothing to non-European makers."
- Possible, not counted: grade-5 s01 H ("unrelated facts" against "Naming two sources proves any claim"), us-history-i s04 A, economics s01 C. Most of the other 170-odd rows fit on reading.

### F3 ("or" tag on one wrong answer)
- grade-2 s01 to s07: rotating-group answer keys end "South (A or B)", "Food, habitat, water cycling or heat movement (B or C)", "Jobs vary (E or F)", "A, I or C", "B, C or D", and so on, in every unit.
- us-government-and-politics s03: "B or C indicates overgeneralization."
- world-geography-and-ancient-civilizations-i s10 ("A or B", "C or I", "D, H or J", "K or C") and s11 ("A or I", "D, L or R", "E, M or T", "F or G").
- world-history-i s04: "One contemporary American empire is O or N." s07: "Error F or H."
- Left out: parallel pairs where each letter fits one half of the answer ("calendar or source-kind error (A or C)", "respectively" forms, grade-1 s02, s03, s05, us-government s06, s08, world-geography I s07, world-history-i s02), and lists of sources or cards ("sources A, B or D").
- Not counted: compound tags such as "(B, G)" or "(A, N)" on a quoted wrong answer or "Does not" sample; 30 units have at least one in field 5 (us-government s01 to s03, us-history-i s02 to s05, world geography I and II, world-history-ii). s03 itself kept "Errors A and L" after its fix, so these were treated as item error lists, not a fault. If the lead counts them, F3 rises well above 12.

### F4 (planned quotation without a free checkable English text)
- world-history-ii s01: Haiti's 1805 constitution article 36, Bolívar's 1815 letter and de Gouges "in our translation" (days 8 to 10 and the assessment); field 10 "our translation".
- world-history-i s08: letters of 1526 and the 1609 edict wait on "a named, published English translation chosen before section 8.3" and "to choose and confirm".
- world-geography-and-ancient-civilizations-i s05: Book of the Dead 125A, "copyrighted translation, brief attributed excerpts only" (not a free checked text; could instead be named and described from the UCL page).
- Checked and clear: world-history-i s06 (Choniates "summarize only"), world-geography II s02, s03, s04 (copyrighted translations, "paraphrase facts only"), us-history-ii s06, world-history-ii s05, s03 (summarize or paraphrase, not quote).

### F5 (end item on our own summary, or an unread source)
Counted for grades 6 to 12 where field 5 gives a real source as "original summary", "paraphrase" or "rendering" and the
item asks students to analyze it as a source (maker, audience, limits, corroboration) while a free or public-domain
text exists, or the source is marked unread or from memory.
- civics s01 (M, plain-word summary of Report 100-565; Aristotle, Polybius "selections from memory, not read"), s02 (plain-word paraphrases of the Declaration of Sentiments), s03 (paraphrase of Burger's reasoning), s08 (summaries of a 1992 account and a current page).
- economics s03 (research account), s05 (federal releases, "original summaries"), s06 ("Unseen primary sources, original summaries" of the 2012 policy statement), s07 (copper report summary), s08 (research summary), s09 (policy card summaries).
- us-history-i s06 (reserved packet "original source summaries", short passages "attached when lessons are made"), s08 ("source selections ... Verify final transcriptions").
- world geography I s07 (Genesis as a "reserved new summary card" though ebible.org text is free), s09 (P1 "original factual summary of the Periplus, sections 7 and 8" while Schoff 1912 is public domain: the s03 case exactly), s10 (Columbus letter, "translation provenance unverified; use original factual summaries").
- world geography II s07 (Final Act II and IV paraphrase, Gutenberg proceedings), s08 (Thucydides 7.27 paraphrase), s09 (Thucydides 1.88 paraphrase), s11 (Frontinus summary), s12 (Eugippius "original summaries").
- world-history-i s01 (Bantu scholarship "not yet read ... attributed paraphrase"), s06, s07 (Luther's letter, 1915 translation read, given as "original attributed summaries"), s08 (summaries pending translation choice), s09 (Nieuhof "original summary"), s10 (packet "original summaries rather than quotations").
- world-history-ii s01 to s08 (reserved packets of "original summaries" or "paraphrases" of identified documents: Haiti and Bolívar, the 1836 factory inspector, Morel 1920 (public domain, "paraphrased only in withheld P1"), the Paris and Versailles passages, Haile Selassie, Deng, the Israeli ministry's report).
- Not counted: elementary packets (kindergarten to grade 5) that adapt a real page or record to the grade's reading level (grade 3 s03, s04, s06, grade 4 s02 to s07, grade 5 s01 to s10, grade 2 s05, s07). The rule asks for a checked passage, but a grade 3 to 5 reader cannot take most primary text, so these need a call, not a count. Also not counted: units whose source is paid-only or "reference only", where the rule asks for a described summary (world geography II s02, s03, s04; world-history-i s04, s05; us-history-i s05).

## 4. How sure

- F1: firm. Each hit shows the feedback and the revision in the row of the day the work is made. Recall is good for rows with minute allocations; prose-only plans may hide more.
- F3: firm on the "or" form as filtered; the parallel-pair exclusions are my reading, and grade-2 rows could be argued as lists. The compound-tag form is not in the count.
- F2: five read and clear; recall is limited to single-letter tags on quoted or "Wrong:" samples, and the match method flags only zero word overlap.
- F4: firm for two, likely for one; only translation notes in field 10 and day rows were searched, so a quotation named without any translation note would be missed.
- F5: the least sure, and the one that moves the band. It rests on a rule reading (end item built on a summary of a free text for source analysis). If only the s03-style cases are kept (summary of a text field 10 marks public domain or free), the count drops to roughly 20 and the union to about 45 (33%), still Off. The source-license check was by field 10 notes, not by opening each source.
- The grade-2 F3 block and the world-history-ii F1 block are the same wording repeated in every unit, so they are cheap to fix together.

## 5. F6, apart

Field 7 has no component-to-move table in any of the 137 units. Each needs one built from its field 5 components and
field 6 letters (the respond day's groups then come from it), and the cap of four groups checked against the units'
respond days. This is a template rule added 2026-11-15, not a fault found in the unit text.

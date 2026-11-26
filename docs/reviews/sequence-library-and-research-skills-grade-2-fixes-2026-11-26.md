# Fixes: scope and sequence of library-and-research-skills-grade-2, 2026-11-26

Fix pass per build/scope-writes/AFTERCORE-FIX.md on the expert read
docs/reviews/sequence-library-and-research-skills-grade-2-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30). The other library reads (kindergarten, grades 1, 3, 4, 5) have no "Across" section; their findings
that touch grade 2 were applied as band items.

Counts: applied 14 (expert 10 findings with every "Settled by the expert" row, band 2, lead calls 2); not applied 0.
13 defect rows logged as fixed (findings 1 to 10, the band turn card item, lead calls 1 and 4); the lens spelling
item goes to the structure pass.

## Applied

- **Expert 1** (days.csv days 7, 8, 11; .md new "Call numbers" bullet, unit 2 arc, skill card and candidates line;
  frame unit 2 What students learn, Days, skill card, evidence, Check set adds): subject by number, then the author's
  letters; nonfiction a subject number over the author's first three letters, fiction a fiction mark over the author's
  letters; the mixed-up shelf and the four-spine item are fiction spines put in order by the author's letters, one
  nonfiction lookup keeps the number; skill card "look it up, copy the label, find the number, then the letters; title
  by author"; no classification system named, pages say "call number".
- **Expert 2** (.md Shorter path): fold-ins 1 and 2 now free their receiving days by moving days 10 and 18 shares and
  self-checks to days 12 and 20; stop pictures in day 9's opening with the source line said inside the show-me (pair
  tries 6 minutes on that path); 20-minute session names what each day sheds (inquiry shares to respond days, day 22's
  member round to 1 minute, day 19 pre-cut cards, day 25 sheet seated alongside, day 27 read once) at 16 working minutes.
- **Expert 3** (days.csv days 10, 11, 19, 25, 27; .md units 2 to 4, check table and "Codes and checks"; frame unit 2,
  3 and 4 evidence and the year-end check cell): day 11 adds the second-kind circle and the respect pointing item (15
  minutes); day 10 ends with one other source-kind card; day 19 adds one "because" (17); day 25 has each child ask the
  teacher-as-person a question and name what one member added (18); day 27 adds the respect item, three cards with one
  "because", and drops ~AASL.IV.B.1 from its codes (18), with the .md naming IV.B.1 as asked in full on day 11.
- **Expert 4** (days.csv days 21 to 24; .md unit 4 arc and skill card bullet; frame unit 4 Days, skill card, seams row):
  day 22 timed 3, 4, 8, 3 minutes with the written first-person answer card when no visitor; day 23 keeps the class
  book retrieval only; the star and wish moves to day 24's opening; the card is held on days 22 and 23 and withdrawn on
  day 24.
- **Expert 5** (days.csv days 7, 10, 18; .md units 2 and 3; frame unit 2 Days and unit 3 host): the printed catalog
  holds 6 to 8 fossil and earth books, day 10 pairs each look up a different one; day 18's stand-alone is "How tall does
  a sunflower grow?".
- **Expert 6** (days.csv days 3, 9; .md unit 1 and 2 load lines; frame unit 1 and 2 Days and seams rows): retrieval
  folded into the show-me (about 2 minutes), pair tries 9 minutes (five questions; three covers).
- **Expert 7** (days.csv days 16, 17 including `retrieves`; .md retrieval paragraph and unit 3; frame unit 3 Days and
  the g1-find-in-a-book seams row): day 16 retrieves the credit line for the two turtle covers, day 17 the find-the-page.
- **Expert 8** (days.csv day 4; .md unit 1 host; frame unit 1 Days): 6 to 8 starred answerable questions; host set
  named by the unit plan.
- **Expert 9** (.md Leave-out): with unit 1 left out, day 13 samples unit 2 in forms not given on day 11 (about 10
  minutes).
- **Expert 10** (days.csv days 1, 5, 16, 18; .md units 1 and 3; frame unit 1 evidence): a spider on its web; the third
  source explains the turtle and sunflower differences by kind, every figure true of a named kind; ela:e2-wh-questions
  weeks 1 to 16 (days 1 to 77).
- **Band, kindergarten finding 3 and grade 3 finding 6** (days.csv day 22; .md unit 4; frame unit 4 Days and the
  g1-group-helpers seams row): the group round opens with SEL's shared talk turn card in the K to 2 words, "eyes look,
  wait my turn".
- **Band, kindergarten stale note** (lens spellings): under For the structure pass (lead call 13).
- **Lead call 1** (frame Placement paragraph and For the lead item 4; .md check placement line): the week 27 after-core
  clash is settled by CALENDAR.md rule 1; scope For the lead item 3 dropped.
- **Lead call 4** (frame Cross-subject ss2-two-accounts cell and unit 3 "Why here" cell): weeks 22 to 23, later than
  this unit; scope For the lead item 1 dropped. Item 2 (school_day) was a statement, already in the .md Calendar
  bullet; dropped. The scope's For the lead now reads "None".

## Not applied

None. Calls 2, 3, 8, 9, 10, 11 and 14 had nothing to act on here (no base text, frame.py passes, begun ids already
`~`, day 25 already reuses day 24's record, no read differs from the frame on a code, no band year). Call 5: the
scope's kinds already follow GLOSSARY and the frame's Day kinds bullet matches.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| School call numbers: subject number over the author's letters for nonfiction, fiction by the author's letters; never "subject letters"; no system named | The form school libraries use; the system's name is a trademark |
| A one-lookup item claims no ~AASL.IV.B.1; add "circle one other kind to try" or drop the code | "More than one kind of source" |
| A unit with no practice day holds its card through the inquiry days before the share and withdraws it on the share day | C7: practice with the card before it goes |
| Folding a retrieval into the show-me as its first case buys pair-try minutes for an owned id | More practice of the owned move without a day added |
| A third source in a "two books differ" set explains why they differ (kind of animal or plant) | "Check, and see why", not "one book was wrong" |

## For the structure pass

- docs/agents/lenses/library.md: "catalogues" to "catalogs", "licences" to "licenses", "judgement" to "judgment"
  (US spelling; lead call 13; kindergarten read stale note).
- data/plans/calendar.csv: no change from this pass (no week moved; checks stay in weeks 13 and 27).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check library-and-research-skills-grade-2`: 0 failures; notes: day 2 is the
  first day for ~AASL.I.A.2 (grade 1 review, correct), "standard None is on no day" for units 3 and 4 (lead call 12,
  left).
- `python -X utf8 scripts/frame.py check library-and-research-skills-grade-2`: 0 failures (4 units, 29 days).
- `python -X utf8 scripts/frame.py calendar`: library grade 2 checks in weeks 13 and 27; no stagger break (library is a
  special, rule 1).

# Fixes: scope and sequence of library-and-research-skills-grade-1, 2026-11-26

Fix pass per build/scope-writes/AFTERCORE-FIX.md on the expert read
docs/reviews/sequence-library-and-research-skills-grade-1-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30). The only other library read so far (kindergarten) has no "Across" section; its findings that
touch grade 1 were applied as band items.

Counts: applied 14 (expert 8 findings with every "Settled by the expert" row, band 2, lead calls 3, own 1); not
applied 0. 13 defect rows logged as fixed (findings 1 to 8, the band turn card item, lead calls 1, 4 and 5, the
source claim).

## Applied

- **Expert 1** (scope-and-sequence.md, Shorter path): 10 days short now counts as about 2 lost sessions wherever they
  fall; fold-ins 1 (day 3 into 4), 2 (day 24 into 25) and 3 (day 29 into 30) rewritten so each receiving day holds 19
  working minutes, with the read's minute splits; the 20-minute session names the item run alongside the seated sheet
  on each check day (whisper walks during the sheet on days 5, 11, 13, 26; day 19's seated copy; day 28's four items
  at about 14 minutes).
- **Expert 2** (days.csv days 1, 2, 4, 5, 13, 28; .md new "Topic first" bullet, unit 1 end line, check 1 and check 2
  lines; frame unit 1 evidence and check cells): topic named by word and plain icon, the "know" box filled before any
  picture or book is opened; marking rule "a fact the icon does not show, true of the topic".
- **Expert 3** (days.csv days 11, 19, 26, 28; .md units 2, 3, 4 and check 2; frame cells): day 11 adds the card-frame
  teacher's page item (about 18 minutes); day 19 stations have each child say a finding and name a helper (about 1.7
  minutes a group), the sticky-note copy is the seated task, the cover-card sort is gone; day 26 whisper walk asks
  "This page taught me ___" and the wish, passage item 9 minutes (about 18 in all); day 28 drops ~AASL.IV.B.1 and the
  .md says why.
- **Expert 4** (days.csv day 22; .md unit 4 arc; frame unit 4 days): picture menu of 6 to 8 answerable wonders, the
  source set written so each has one answering page.
- **Expert 5** (days.csv day 27; .md unit 4; frame unit 4 respond): 6, 2, 2, 9 minute split with partner telling.
- **Expert 6** (.md Leave-out): unit 1 left out, day 10 opens with the one-step know and wonder form claiming nothing;
  day 13 samples unit 2 on new forms (about 11 minutes).
- **Expert 7** (days.csv days 9, 10; .md unit 2; frame unit 2 tools): the teacher's page is the unit's tree-roots
  read-aloud page on the Curio Class site, printed in the card frame on the paper path; any other page gets the swap
  note.
- **Expert 8** (days.csv days 4, 29, 30; .md retrieval table): day 4 `retrieves` cleared (k-wonder: day 2 only), and
  the .md's "opens with a retrieval" line now says most days and names the empty column; day 29 adds ~AASL.V.C.1;
  day 30 drops g1-class-book from `skills` (the book is reread, not made, so ~AASL.I.B.3 is not claimed there).
- **Band, kindergarten read finding 3** (days.csv day 16; .md retrieval table): the k-talk-in-group retrieval opens
  with the shared turn card's two pictures in SEL's words, "eyes look, wait my turn".
- **Band, kindergarten read stale note** (lens spellings): listed under For the structure pass (lead call 13).
- **Lead call 1** (frame Placement paragraph and For the lead item 3): reworded as settled by CALENDAR.md rule 1;
  scope For the lead item 2 dropped; the .md Weeks line says shared after-core weeks are settled by the same rule.
- **Lead call 5** (frame Day kinds bullet and unit 4 Days list): star-and-wish pair work is an inquiry day (GLOSSARY);
  practice days named as 2, 8 and 17; scope For the lead item 1 dropped and the Kinds bullet reworded.
- **Lead call 4** (frame Sensitivity reads; .md Sources not loaded): the frame said the online-safety presentation
  states the trusted-adult rule; the listing the read opened does not, and the file was not read. Both now say
  nothing rests on it.
- **Own** (days.csv day 29): ~AASL.IV.B.1 dropped from day 29 as well, since it reteaches day 28's one-source item;
  logged with finding 8.

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A know and wonder item names the topic by word and plain icon and opens the picture after the "know" box; mark "a fact the icon does not show" | AASL.I.A.2's "before you start looking"; a picture lets a child pass by looking |
| A grade 1 station claiming III.D.1 has every child say a finding; jobs are for handling cards | The id is asked of every child |
| A one-source item does not claim IV.B.1; add a second kind of place or drop the code | "More than one kind of source" |
| A respond day that rereads a product does not claim the product's skill | Rereading is not making |
| 20-minute session for day 19: stations at about 1.3 minutes a group (each child's finding and helper turn kept, transitions cut), sticky-note copy seated alongside, about 14 minutes | The read named the seated copy but not the station time; 17 minutes of stations cannot fit 14 working minutes |
| Once-a-week course, 10 days short = about 2 lost sessions, covered by named fold-ins | Arts scope lead call |

## For the structure pass

- docs/agents/lenses/library.md: "catalogues" to "catalogs", "licences" to "licenses", "judgement" to "judgment"
  (US spelling; lead call 13; kindergarten read stale note).
- data/plans/calendar.csv: no change from this pass (no week moved; checks stay in weeks 13 and 28).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check library-and-research-skills-grade-1`: 0 failures; notes "standard None
  is on no day" for units 2 to 4 (lead call 12, left).
- `python -X utf8 scripts/frame.py check library-and-research-skills-grade-1`: 0 failures (4 units, 30 days).
- No unit, day count, owned row or week changed, so the stagger is as before (library is a special, outside rule 1).
